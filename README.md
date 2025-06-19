<p align="center">
  <a href="https://esim.fossee.in/">
    <img src="https://img.shields.io/badge/eSim-FOSSEE-F28C28?style=for-the-badge&logo=ubuntu&logoColor=white" alt="eSim Badge"/>
  </a>
  <a href="https://openroad.readthedocs.io/en/latest/">
    <img src="https://img.shields.io/badge/OpenROAD-RTL%20to%20GDSII-FF2222?style=for-the-badge&logo=open-access&logoColor=white" alt="OpenROAD Badge"/>
  </a>
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge"/>
  </a>
  <a href="https://ubuntu.com/">
    <img src="https://img.shields.io/badge/Ubuntu-Linux-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu Badge"/>
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.18-F7DF1E?style=for-the-badge&logo=python&logoColor=blue" alt="Python Badge"/>
  </a>
</p>


# 🚀 eSim to OpenROAD Automation & SPICE to Verilog Converter

This project brings together two critical EDA tasks under a single repository:

1. 🔄 **SPICE to Verilog conversion** of digital circuits designed using eSim
2. 🛠️ **End-to-End RTL to GDSII flow** using OpenROAD for circuits originating in eSim

<p align="center">
  <img src="https://github.com/user-attachments/assets/aae87d6d-0f3a-4f18-8d1e-09d5e0f6ad1a" width="49%" height=300>
  <img src="https://github.com/user-attachments/assets/b4743e55-e26c-44b8-aac1-e8bec6860715" width="49%" height=300>
</p>


These tasks demonstrate the bridge between circuit design, behavioral description, and physical layout—all using open-source tools.

---

## 📑 Table of Contents

- [🚀 eSim to OpenROAD Automation & SPICE to Verilog Converter](#-esim-to-openroad-automation--spice-to-verilog-converter)
- [📘 Introduction](#-introduction)
- [📐 About eSim](#-about-esim)
- [🧱 About OpenROAD](#-about-openroad)
- [🛠️ eSim Installation Instructions (v2.3)](esim-installation-instructions-(v2.3))
- [🔑 Openlane Installation Instructions](#-openlane-installation-instructions)

### 🔧 Task 1: SPICE to Verilog Converter
- [🎯 Objective](#-objective)
- [📢 Instructions](#-instructions)
- [🛠️ Methodology](#️-methodology)
- [🧩 Errors Encountered & Solutions](#-errors-encountered--solutions)
- [🔧 Steps to Run `sp2vlog.py` (SPICE to Verilog Converter)](#-steps-to-run-sp2vlogpy-spice-to-verilog-converter)
- [📁 Files Included](#-files-included)

### 🔧 Task 2: eSim to OpenROAD Full Flow Automation
- [🎯 Objective](#-objective-1)
- [📢 Instructions](#-instructions-1)
- [🛠️ Methodology](#️-methodology-1)
- [🧩 Errors Encountered & Solutions](#-errors-encountered--solutions-1)
- [⚙️ Detailed Functionality of `Simroad.py` – The Automation Script](#-detailed-functionality-of-simroadpy--the-automation-script)
- [🚀 Steps to Run `Simroad.py`](#-steps-to-run-simroadpy)
- [📁 Files Included](#-files-included-1)

- [🗂 Folder Structure](#-folder-structure)
- [🧰 Tools & Tech Stack](#-tools--tech-stack)
- [🧑‍💻 Author](#-author)
- [📜 License](#-license)
- [🙌 Acknowledgements](#-acknowledgements)

---

## 📘 Introduction

In the rapidly evolving field of VLSI design, seamless integration between analog and digital design tools is essential for efficient and accurate chip development. SPICE (Simulation Program with Integrated Circuit Emphasis) has long been the backbone of analog circuit simulation, enabling designers to validate the behavior of circuits at the transistor level. However, as digital design flows increasingly rely on automation and standardization, converting SPICE netlists into Verilog becomes a powerful bridge—allowing low-level circuit behavior to be incorporated into high-level RTL design and physical synthesis workflows. This SPICE-to-Verilog conversion is not just a convenience; it represents a significant leap toward unifying traditionally siloed analog and digital domains. It empowers designers to reuse and validate SPICE-defined blocks within digital toolchains, ensuring consistency across simulations, synthesis, and layout stages.

In parallel, the automation of design flows from tools like eSim (for schematic capture and SPICE netlist generation) to OpenROAD (for RTL-to-GDSII implementation) revolutionizes the VLSI design landscape. This open-source pipeline allows students, researchers, and startups to design, simulate, synthesize, and generate layouts without relying on costly proprietary tools. By bridging these tools with custom scripts and converters, we unlock a fully open-source end-to-end VLSI workflow—capable of transforming a simple schematic into a fabricated-ready layout with minimal manual intervention. Such automation reduces design time, increases reproducibility, and democratizes silicon development for a broader community. This repository implements and automates the following two tasks:

- **Task 1:** Converts SPICE netlists (exported from eSim) to structurally correct Verilog
- **Task 2:** Automates the entire RTL to GDSII flow using OpenROAD for Verilog files generated from eSim

All the scripting is done using Python, and tools used are fully open-source, making the flow reproducible and accessible.

---

## 📐 About eSim

**eSim** (previously known as Oscad / FreeEDA) is a free/libre and open source EDA tool developed by FOSSEE, IIT Bombay for circuit design, simulation, analysis and PCB design. It is an integrated tool built using free/libre and open source software such as KiCad, Ngspice and GHDL. eSim is released under GPL. eSim offers similar capabilities and ease of use as any equivalent proprietary software for schematic creation, simulation and PCB design, without having to pay a huge amount of money to procure licenses. Hence it can be an affordable alternative to educational institutions and SMEs. It can serve as an alternative to commercially available/licensed software tools like OrCAD, Xpedition and HSPICE.

![image](https://github.com/user-attachments/assets/89a47d4c-f499-4291-ad49-326eb118ec62)

*The eSim simulation tool*

### 🔮 Features of eSim

- Draw circuits using KiCad, create a netlist and simulate using Ngspice.
- Design PCB layouts and generate Gerber files using KiCad.
- Add/Edit device models(Spice Models) and subcircuits using the Model Builder and Subcircuit Builder tools.
- Perform Mixed-Signal Simulation.
- Support for Ubuntu OS and Windows OS.

---

## 🧱 About OpenROAD

OpenROAD is an open-source project that provides a fully automated digital VLSI back-end toolchain—starting from RTL synthesis to GDSII layout generation. It focuses on developing the actual EDA tools like OpenDB, TritonRoute, FastRoute, OpenSTA, etc., that perform tasks such as floorplanning, placement, clock tree synthesis, routing, and timing analysis. OpenROAD™ is a front-runner in open-source semiconductor design automation tools and know-how. This project reduces barriers of access and tool costs to democratize system and product innovation in silicon. The OpenROAD tool and flow provide autonomous, no-human-in-the-loop, 24-hour RTL-GDSII capability to support low-overhead design exploration and implementation through tapeout. We welcome a diverse community of designers, researchers, enthusiasts and entrepreneurs who use and contribute to OpenROAD to make a far-reaching impact.

![image](https://user-images.githubusercontent.com/86701156/124007394-f62a0d80-d9f8-11eb-9d46-7cc885c0eff6.PNG)

*The Openlane Full ASIC flow*

OpenLane, on the other hand, is a higher-level integration framework or "flow wrapper" built around OpenROAD and other open-source tools (like Yosys, Magic, Netgen). It provides scripts and automation to help users run a complete RTL-to-GDSII flow using these underlying tools with minimal configuration. It is an automated RTL to GDSII flow based on several components including OpenROAD, Yosys, Magic, Netgen, CVC, SPEF-Extractor, KLayout and a number of custom scripts for design exploration and optimization. It also provides a number of custom scripts for design exploration and optimization.The flow performs all ASIC implementation steps from RTL all the way down to GDSII. OpenLane abstracts the underlying open source utilities, and allows users to configure all their behavior with just a single configuration file.


### 📦 OpenROAD vs. OpenLane – Clarified
OpenROAD and OpenLane are two key projects within the open-source silicon ecosystem, working together to enable a full RTL-to-GDSII flow. OpenROAD provides the core back-end EDA tools required for digital physical design, including placement, routing, and timing analysis. It is a toolkit of standalone, modular engines meant for physical implementation. OpenLane, in contrast, serves as the orchestration layer that ties these tools into a cohesive, automated design flow. It integrates tools from OpenROAD along with synthesis (Yosys), layout (Magic), and verification (Netgen) components, offering a simplified user experience. Essentially, OpenROAD is the engine, and OpenLane is the vehicle that drives it. Together, they allow designers to take a digital RTL design and produce a manufacturable GDSII layout using only open-source solutions—significantly lowering the entry barrier to ASIC design and fabrication. We have used the OpenLane wrapper for OpenROAD in this project.

---


## 🛠️ eSim Installation Instructions (v2.3)

---

### 📚 Table of Contents
1. [eSim Installation on Ubuntu (Linux)](#1-esim-installation-on-ubuntu-linux)  
2. [eSim Installation on Windows](#2-esim-installation-on-windows)  
3. [How to Run eSim](#how-to-run-esim)  
4. [Note](#note)

---

### 1. 🚀 eSim Installation on Ubuntu (Linux)

#### 🧩 Steps:
1. After downloading the eSim archive, extract it:
   ```bash
   unzip eSim-2.3.zip
   ```

2. Change directory to the top-level `eSim` directory (where this `INSTALL` file is located):
   ```bash
   cd eSim-2.3
   ```

3. To install eSim and all required dependencies:
   ```bash
   chmod +x install-eSim.sh
   ./install-eSim.sh --install
   ```

4. To uninstall eSim and all its components:
   ```bash
   ./install-eSim.sh --uninstall
   ```

---

### 2. 💻 eSim Installation on Windows

#### 🧩 Steps:
1. Download eSim for Windows from https://esim.fossee.in/  
   ⚠️ Important: Disable antivirus software during installation.

2. If MinGW and/or MSYS are already installed, remove them from the PATH environment variable to avoid conflicts.

3. Run the eSim installer by double-clicking the `.exe` file and follow the instructions.

4. After installation, download and place this file into the eSim home directory (`FOSSEE\eSim\`):  
   TerminalUi.ui → https://github.com/FOSSEE/eSim/blob/master/src/frontEnd/TerminalUi.ui#L6

5. Download and add the following executable into the `nghdl` folder (`FOSSEE\eSim\nghdl\src`):  
   Executable: https://drive.google.com/file/d/17MNCCq9cG6A7fnIH-4KMUMY-yb4rW9s4/view?usp=sharing

6. Installation is now complete!

7. To uninstall eSim, run `uninst-eSim.exe` located in the top-level eSim directory.

---

### 📦 How to Run eSim

#### A. From Terminal (Linux)
```bash
esim
```

#### B. From Desktop
- Double-click on the eSim desktop icon

---

### 📝 Note

If you face any installation issues, please report them at:  
https://forums.fossee.in/

---

## 🔑 Openlane Installation Instructions

1. `git clone https://github.com/nickson-jose/openlane_build_script`
2. `sudo -i` #switch to root user (or have root user password ready).
3. Change directory to where openlane_build_script folder was cloned. `cd /path/to/openlane_build_script`
4. Execute the script as below:

      - **For standalone build**
       
        - `chmod 775 openlane_script.sh`
        - `./openlane_script.sh`
     
      - **For build in conjunction with vsdflow**
       
        -  Copy the `openlane_script_wo_depends.sh` to vsdflow folder.
        - `chmod 775  openlane_script_wo_depends.sh`
        - `./openlane_script_wo_depends.sh`
      
5. This script would create following directory structure:

- **For build in conjunction with vsdflow**
```bash 
vsdflow/
  └── work
     └── tools
      ├── cmake-3.13.0
      ├── cmake-3.13.0.tar.gz
      ├── graywolf
      ├── magic-8.3.50
      ├── magic-8.3.50.tgz
      ├── netgen-1.5.134
      ├── netgen-1.5.134.tgz
      ├── openlane_working_dir
      ├── OpenSTA
      ├── OpenTimer
      ├── qflow-1.3.17
      ├── qflow-1.3.17.tgz
      ├── qrouter-1.4.59
      ├── qrouter-1.4.59.tgz

```
- **For standalone build**
 ```bash  
 Desktop/
 ...
  └── work
    └── tools 
        └── openlane_working_dir
         |__ Openlane
                       
```              
 
### 📝Steps To Run Openlane

1. Go to /path/to/openlane (i.e., ~/work/tools/openlane_working_dir/Openlane)
2. There are two ways of invoking openlane. The easiest of the two would be:
   - `make mount`

   The second way would be to explicitly specify the path to PDK_ROOT and OPENLANE_IMAGE_NAME and invoking docker with these inputs
   - `export PDK_ROOT=<absolute path to where skywater-pdk and open_pdks reside>`
   - `export OPENLANE_IMAGE_NAME=<docker image name>`
   - `docker run -it -v $(pwd):/openlane -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) $OPENLANE_IMAGE_NAME`
   
3. **Note:** If you face "permission denied" during docker invocation in setup or in above step, do refer below link to resolve:
   - [Fix Docker Permission Denied Issue](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)

4. `./flow.tcl -design spm`
(the above flow.tcl command will run RTL2GDS flow for design named "spm". Same can be done for other designs which are present in ~/work/tools/openlane_working_dir/Openlane/designs)

5. Refer to: https://github.com/efabless/openlane for detailed instructions.

---

## 📌 Task 1: SPICE to Verilog Converter

### 🎯 Objective

Write a Python script to convert a SPICE netlist generated by eSim into a Verilog file compatible with OpenROAD.

### 📢 Instructions

1. Use eSim to design a simple digital circuit (e.g., an inverter or 2-input NAND gate).
2. Export the SPICE netlist from eSim.
3. Write a Python script that:
4. Reads the SPICE netlist.
5. Converts it into a Verilog module, mapping components (e.g., transistors) to Verilog equivalents.
6. Handles inputs, outputs, and basic gates.
7. Test the script with your circuit and ensure the Verilog file is syntactically correct.


### 🛠️ Methodology

1. **Circuit Design:** A half-adder was designed in eSim using standard digital gates in the eSim library (d_and , d_xor)
2. **Netlist Export:** The netlist was exported from eSim in the `cir` SPICE format.
3. **Parsing Logic:** A Python script (`sp2vlog.py`) was written to:
   - Parse `.cir` netlist lines
   - Identify if the device names are present in the Logical Cells Array, if not include unknown design files at the top
   - Extract transistors, gate types, connectivity
   - Ensure clean input and output descriptions
   - Map SPICE structures to structural Verilog modules
   - Extract synthesizable verilog code
   - Store it in a verilog file in the directory
4. **Output:** A valid `.v` Verilog file was generated with the appropriate module, ports, and gate instantiations.

### 🧩 Errors Encountered & Solutions

| Issue | Description | Resolution |
|-------|-------------|------------|
| `command not found` on SPICE export | eSim exported netlist with title text and non-SPICE formatting in the first few lines, which confused the parser when treated as commands | Filtered out non-SPICE lines and ensured parsing only starts after valid `.subckt` or device definitions |
| Ambiguous port identification | The SPICE netlist did not explicitly mark inputs/outputs, making it hard to define `input` and `output` ports in the Verilog module | Counted node occurrences; nodes appearing only once were treated as primary inputs/outputs for initial mapping |
| Undefined component models | SPICE netlist included analog or passive components (like `Vdd`, `GND`, or `.model` statements) that do not translate to Verilog constructs | Skipped lines that didn’t represent digital logic elements; filtered using regex and logic-based checks |
| MOSFET logic mapping | SPICE defined logic using NMOS/PMOS at the transistor level, which doesn't directly map to Verilog gate-level primitives | Only supported pre-defined gate instances (`d_and`, `d_or`, `d_inv`, etc.) generated by eSim digital library |
| Capitalization/format errors | Netlist had inconsistent capitalization and formatting (e.g., `D_AND`, `d_and`, extra spaces), which affected parsing | Used regular expressions and `.lower()` normalization; removed extra whitespace to standardize component names |

### 🔧 Steps to Run `sp2vlog.py` (SPICE to Verilog Converter)

Follow the steps below to clone the repository, navigate to the appropriate directory, and convert your `.spice` or `.cir` netlist to a Verilog module.

---

✅ 1. Clone the Repository

```bash
git clone https://github.com/AdityaMino.git
```

📁 2. Navigate to the Repository Directory

```bash
cd Task1_sp2vlog
```

🚀 3. Run the Converter Script

```bash
python3 sp2vlog.py
```
You will be prompted:

```css
📂 Enter full path to your .spice or .cir file:
```
Type the full path or relative path to your file, in my case it was:

```bash
/home/vboxuser/Downloads/halfadder.cir
```

📄 4. Output
The generated Verilog file will be created in a clean subdirectory with the same cleaned name as your netlist. For example:

```css
sp2vlog/
├── sp2vlog.py
├── halfadder.cir
└── halfadder/
    └── halfadder.v
```
✅ Requirements

- Python 3.x installed
- No external Python dependencies required

### 📁 Files Included

- `Task1_sp2vlog/sp2vlog.py`
- `Task1_sp2vlog/example_netlist.cir`
- `Task1_sp2vlog/generated_verilog.v`

---

## 📌 Task 3: eSim to OpenROAD Full Flow Automation

### 🎯 Objective

Design a circuit in eSim, simulate it, and use OpenROAD to generate a physical layout.

### 📢 Instructions

1. Design a simple digital circuit (e.g., half-adder or multiplexer) in eSim.
2. Simulate the circuit in eSim to verify functionality (e.g., logic behavior or timing).
3. Export the design as a Verilog file.
4. Use OpenROAD to perform synthesis, placement, and routing to generate a physical layout.
5. Write a python script to automate the process.
6. Document each step, including issues and resolutions.


### 🛠️ Methodology

1. **Schematic Design:** A half-adder circuit was designed and simulated in eSim using basic gates.
2. **Simulation Validation:** Output waveforms were saved to ensure functional correctness.
3. **Verilog Export:** The eSim design was exported to a synthesizable Verilog format.
4. **Automation Script:** A Python script (`Simroad.py`) was created to:
   - Ask the user for OpenLane path
   - Copy Verilog files into `design/` folder inside OpenROAD
   - Generate `config.tcl` and run OpenROAD scripts via `subprocess`
   - Collect and store GDS, DEF, logs, and other outputs
5. **Layout Review:** The GDS file was opened using Klayout for visual inspection.

### 🧩 Errors Encountered & Solutions

| Issue | Description | Resolution |
|-------|-------------|------------|
| **Missing "Convert to Verilog" in eSim GUI** | In certain installations or older versions of eSim, the "Convert to Verilog" option was either missing or unresponsive in the GUI. This caused confusion and delayed the export process. | We bypassed this by manually accessing the SPICE netlist and applying a custom Python conversion script to extract a clean Verilog version from it. Alternatively, users were guided to copy netlists directly from the schematic directory. |
| **KLayout auto-launch failures** | When attempting to auto-launch KLayout after the OpenROAD flow, it failed on some systems—especially headless VMs or environments without GUI support. This led to script hangs or unclear errors. | Instead of forcing GUI execution, we replaced it with clear and structured instructions on how to open the GDS manually using KLayout: `Open → final.gds`. |
| **Hardcoded OpenROAD path** | The initial script had the OpenROAD path hardcoded to a specific location (e.g., `~/Desktop/...`). This made it unusable for other users with different setups and paths. | Replaced static path with dynamic user input using `input()` and `Path().resolve()`, making the script adaptable to any OpenROAD installation. |
| **File not found errors** | Several early errors stemmed from assumptions about directory structure (e.g., assuming `design/` or `src/` always existed). This caused `FileNotFoundError` exceptions during execution. | Introduced error-handling and used `os.makedirs(..., exist_ok=True)` and `os.path.join()` / `Pathlib` to dynamically ensure the paths exist before performing operations. |
| **Output clutter** | The console output from subprocess calls and other logs were verbose and unformatted, making it hard for users to follow what was happening. | Enhanced UX by adding emojis, green/red color-coded info/error messages, and spacing to maintain clarity throughout the terminal output. |
| **No modular structure in exported Verilog** | The Verilog generated (manually or by script) from SPICE often lacked modular boundaries or clean port definitions, making it incompatible with synthesis tools. | Manually refactored the Verilog file by ensuring each design had proper `module`, `endmodule`, and explicit `input`/`output` declarations. The conversion script was updated to assist in auto-wrapping logic as needed. |

###  

`Simroad.py` automates the flow from a Verilog file (exported from eSim) to a physical layout using OpenROAD through the OpenLane wrapper. I have listed below all the precise steps it performs:

#### 🔹 1. **Prompt the User for OpenLane Installation Path**
- **Why:** OpenLane installations can vary across systems.
- **How:** Uses `input()` and `Path().resolve()` to capture and normalize the path from the user.
- **Code Snippet:**
  ```python
  openlane_path = Path(input("Enter path to OpenLane directory: ")).expanduser().resolve()
  ```



#### 🔹 2. **Create a Working Design Directory Inside OpenLane**
- **Why:** OpenLane expects each design to reside under `design/<design_name>`.
- **How:** Uses `os.makedirs()` to create the directory if it doesn't exist.
- **Effect:** Prepares an isolated workspace for the design flow.
- **Code Snippet:**
  ```python
  design_dir = openlane_path / "design" / "esim_design"
  os.makedirs(design_dir, exist_ok=True)
  ```



#### 🔹 3. **Copy Verilog File from eSim to OpenLane**
- **Why:** OpenLane requires Verilog files to be placed inside `src/` under the design directory.
- **How:** Uses `shutil.copy()` after creating the `src/` folder.
- **Code Snippet:**
  ```python
  (design_dir / "src").mkdir(parents=True, exist_ok=True)
  shutil.copy("half_adder.v", design_dir / "src" / "half_adder.v")
  ```



#### 🔹 4. **Generate `config.tcl` for OpenLane**
- **Why:** OpenLane uses this config to know the design name, top module, clock details, etc.
- **How:** The script writes this file using Python's file I/O.
- **Example `config.tcl`:**
  ```tcl
  set ::env(DESIGN_NAME) esim_design
  set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/*.v]
  set ::env(CLOCK_PORT) clk
  set ::env(CLOCK_PERIOD) 10.0
  ```



#### 🔹 5. **Run OpenLane Flow Using `subprocess`**
- **Why:** To execute synthesis, placement, routing, and GDS export.
- **How:** Runs the following inside OpenLane root:
  ```bash
  ./flow.tcl -design esim_design
  ```
- **Effect:** Starts a full RTL-to-GDSII flow using OpenROAD’s backend tools.



#### 🔹 6. **Collect GDS and Result Files**
- **Why:** To organize and present final outputs like `.gds`, `.def`, `.log`, etc.
- **How:** Copies them from OpenLane’s `runs/` directory to a local `outputs/` directory.
- **Code Snippet:**
  ```python
  shutil.copy(openlane_path / "runs" / "esim_design" / "results" / "final.gds", "./outputs/")
  ```
  ```bash
    ✅ GDS file generated successfully: ./outputs/final.gds
  📂 To view layout: Open in KLayout using the command 'klayout design_name.gds'
  ```
---

Hence `Simroad.py` script streamlines the full design flow from eSim’s schematic export to OpenROAD layout generation. It eliminates manual steps, reduces user error, and enables fully open-source RTL-to-GDSII automation—making it ideal for education, prototyping, and research in VLSI design.

### 🚀 Steps to Run `Simroad.py`

A concise guide to run the automated RTL-to-GDS flow using **Simroad.py**.


## 🧾 Prerequisites

- ✅ eSim installed (https://esim.fossee.in/)
- ✅ OpenLane setup with Docker support
- ✅ Ubuntu Linux OS (recommended)
- ✅ Python ≥ 3.0


1. Clone the repository

```bash
git clone https://github.com/your-username/simroad.git
cd simroad
```

2. Run the script

```bash
python3 Simroad.py
```

3. Input required:
    → Full path to your Verilog file (e.g., /home/user/Desktop/halfadder.v)
    → OpenLane toolchain path (e.g., ~/Desktop/openlane_build_script/work/tools/openlane_working_dir/OpenLane)

4. Let the flow run (synthesis, floorplanning, placement, CTS, routing, etc.)

5. On success, 'reports' and 'results' directories will be created in the SAME folder as your Verilog file.


---

#### 🖼️ View GDS in KLayout

# 1. Open a terminal and go to OpenLane folder:
```bash
cd ~/Desktop/openlane_build_script/work/tools/openlane_working_dir/OpenLane
```

2. Launch Docker in interactive mode:
```bash
make mount
```

3. Navigate to the GDS directory inside Docker:

```bash
cd designs/<your_design>/runs/<latest_run>/results/final/gds
```

4. View your layout using KLayout:
klayout <design_name>.gds

---


✅ That’s it! You've successfully completed the RTL to GDSII flow with **Simroad**.


### 📁 Files Included

- `Task2_Simroad/Simroad.py`
- `halfadder/schematic.sch`, `example.v`, and `simulation_result.png`
- `openroad_output/layout.gds`, `results.log`

---

## 🗂 Folder Structure

```
esim-to-openroad-automation/
├── README.md
├── LICENSE
├── .gitignore
├── Task1_sp2vlog/
│   ├── sp2vlog.py
│   ├── halfadder.cir
│   ├── halfadder.v
├── Task3_Simroad/
│   ├── Simroad.py
│   ├── halfadder/
│   │   ├── halfadder.sch
│   │   ├── halfadder.v
│   │   └── simulation_result.png
│   ├── openroad_output/
│   │   ├── layout.gds
│   │   └── results.log

```


## 🧰 Tools & Tech Stack

| Tool        | Purpose                        |
|-------------|--------------------------------|
| **eSim**    | Schematic design, SPICE export |
| **NgSpice** | Simulation backend for eSim    |
| **Python 3**| Automation and netlist parsing |
| **OpenROAD**| Full RTL to GDS flow           |
| **OpenLane**| Wrapper for OpenROAD automation|
| **Klayout** | GDS viewing and verification   |

---

## 🧑‍💻 Author

- **Name:** [Aditya Minocha]
- **Email:** [adityaminocha10@gmail.com]
- **GitHub:** [https://github.com/AdityaMino](https://github.com/AdityaMino)

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for full terms.

---

## 🙌 Acknowledgements

- Mr. Sumanto Kar - Assistant Project Manager, FOSSEE IIT Bomay
- Mr. Kanan Moudgalya - Emeritus Fellow, IIT Bombay
- **FOSSEE, IIT Bombay** – for developing eSim and promoting open-source EDA
- **The OpenROAD Project** – for enabling accessible, full-stack digital ASIC design
- **The Klayout Community** – for providing an excellent GDSII viewer
- All open-source contributors and communities who made these tools possible
- [efabless openlane team](https://github.com/efabless/openlane)
