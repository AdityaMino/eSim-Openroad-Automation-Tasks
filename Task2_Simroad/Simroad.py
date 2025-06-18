import os
import shutil
import subprocess
from pathlib import Path

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def info(msg):
    print(f"{GREEN}ℹ️  [INFO] {msg}{RESET}")

def error(msg):
    print(f"{RED}❌ [ERROR] {msg}{RESET}")

def highlight(msg):
    print(f"{BLUE}{BOLD}{msg}{RESET}")

def klayout_note(msg):
    print(f"{YELLOW}{msg}{RESET}")

def get_design_name(verilog_path):
    return Path(verilog_path).stem

def prepare_design_files(verilog_path, openlane_dir):
    verilog_path = Path(verilog_path).resolve()
    if not verilog_path.exists():
        raise FileNotFoundError(f"Verilog file does not exist: {verilog_path}")

    design_name = get_design_name(verilog_path)
    design_dir = Path(openlane_dir) / "designs" / design_name
    src_dir = design_dir / "src"

    info(f"Creating design directory for: {design_name}")
    src_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy(verilog_path, src_dir / verilog_path.name)

    with open(verilog_path, 'r') as f:
        verilog_contents = f.read()
    has_clk = "clk" in verilog_contents and "input" in verilog_contents

    config_lines = [
        f'set ::env(DESIGN_NAME) "{design_name}"',
        'set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/*.v]',
        'set ::env(SDC_FILE) [glob $::env(DESIGN_DIR)/*.sdc]',
        'set ::env(FP_CORE_UTIL) 1',
        'set ::env(PL_TARGET_DENSITY) 0.5',
    ]
    if has_clk:
        config_lines.insert(3, 'set ::env(CLOCK_PORT) "clk"')
        config_lines.insert(4, 'set ::env(CLOCK_PERIOD) "10.0"')

    with open(design_dir / "config.tcl", "w") as f:
        f.write("\n".join(config_lines))

    sdc = """
create_clock -name clk -period 10.0 [get_ports clk]
set_input_delay 2.0 -clock clk [all_inputs]
set_output_delay 2.0 -clock clk [all_outputs]
""".strip() if has_clk else ""

    with open(design_dir / f"{design_name}.sdc", "w") as f:
        f.write(sdc)

    info(f"Design files are ready at {design_dir}")
    return design_name

def run_openlane_flow(openlane_dir, design_name):
    os.chdir(openlane_dir)
    info("Launching OpenLane using Docker... 🐳")

    docker_image = "efabless/openlane:e73fb3c57e687a0023fcd4dcfd1566ecd478362a-amd64"

    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{openlane_dir}:/openlane",
        "-v", f"{Path.home()}/.volare:/home/openlane/.volare",
        "-e", "PDK=sky130A",
        "-e", "PDK_ROOT=/home/openlane/.volare",
        docker_image,
        "bash", "-c", f"cd /openlane && ./flow.tcl -design {design_name}"
    ]

    result = subprocess.run(docker_cmd)
    if result.returncode != 0:
        error("OpenLane flow failed to run.")
    else:
        info("✅ OpenLane flow completed successfully ")

def print_results(openlane_dir, design_name):
    from datetime import datetime

    runs_dir = Path(openlane_dir) / "designs" / design_name / "runs"
    run_folders = sorted(runs_dir.glob("RUN_*"))
    if not run_folders:
        error("No run directory found. Flow may have failed.")
        return
    latest_run = run_folders[-1]

    gds_file = latest_run / "results/final/gds" / f"{design_name}.gds"
    reports_dir = latest_run / "reports"
    results_dir = latest_run / "results"

    desktop_dir = Path.home() / "Desktop"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_dir = desktop_dir / f"{design_name}_OpenLane_Output_{timestamp}"
    dest_dir.mkdir(parents=True, exist_ok=True)

    if reports_dir.exists():
        shutil.copytree(reports_dir, dest_dir / "reports", dirs_exist_ok=True)
        info(f"📄 Reports copied to: {dest_dir / 'reports'}")
    else:
        error("Reports directory not found.")

    if results_dir.exists():
        shutil.copytree(results_dir, dest_dir / "results", dirs_exist_ok=True)
        info(f"📦 Results copied to: {dest_dir / 'results'}")
    else:
        error("Results directory not found.")

    if gds_file.exists():
        info(f"✅ GDS File Generated: {gds_file}\n\n")
        klayout_note("💡️ To view the GDS file manually using KLayout, follow these steps:\n")

        klayout_note("[1] Open a terminal on your host and run:")
        klayout_note("    cd ~/Desktop/openlane_build_script/work/tools/openlane_working_dir/OpenLane\n")

        klayout_note("[2] Launch the OpenLane Docker container in interactive mode:")
        klayout_note("    make mount\n")

        klayout_note("[3] Inside the container, go to:")
        klayout_note(f"    cd designs/{design_name}/runs/{latest_run.name}/results/final/gds\n")

        klayout_note(f"[4] Open GDS with KLayout:")
        klayout_note(f"    klayout {design_name}.gds\n")

        klayout_note("\n🎉 Done! Your layout will open in KLayout.")
    else:
        error("GDS file not found.")

def main():
    print("\n")
    highlight("\t\t\t  🎯 WELCOME TO SIMROAD 🎯\n")
    highlight("\t\tAn Automated RTL ➜ GDSII Flow from eSim to OpenROAD\n")

    verilog_path = input("📂 Enter full path to your Verilog file: ").strip()
    user_input = input("📂 Enter the full path to your OpenLane directory: ").strip()
    openlane_path = Path(user_input).expanduser().resolve()

    try:
        design_name = prepare_design_files(verilog_path, openlane_path)
        run_openlane_flow(openlane_path, design_name)
        print_results(openlane_path, design_name)
    except Exception as e:
        error(str(e))

if __name__ == "__main__":
    main()

