import os
import re

# Logic cells with no vdd/vss
LOGIC_CELLS = {
    "d_and": {
        "ports": ["in1", "in2", "out"],
        "behavior": "assign out = in1 & in2;"
    },
    "d_or": {
        "ports": ["in1", "in2", "out"],
        "behavior": "assign out = in1 | in2;"
    },
    "d_inv": {
        "ports": ["in", "out"],
        "behavior": "assign out = ~in;"
    },
    "d_nand": {
        "ports": ["in1", "in2", "out"],
        "behavior": "assign out = ~(in1 & in2);"
    },
    "d_nor": {
        "ports": ["in1", "in2", "out"],
        "behavior": "assign out = ~(in1 | in2);"
    },
    "d_xor": {
        "ports": ["in1", "in2", "out"],
        "behavior": "assign out = in1 ^ in2;"
    },
    "d_xnor": {
        "ports": ["in1", "in2", "out"],
        "behavior": "assign out = ~(in1 ^ in2);"
    },
    "d_buf": {
        "ports": ["in", "out"],
        "behavior": "assign out = in;"
    }
}

def parse_spice(filename):
    print(f"🔍 Parsing SPICE netlist: {filename}")
    with open(filename, 'r') as f:
        lines = f.readlines()

    top_instances = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('*'):
            continue
        if re.match(r"^[UuXx]", line):
            top_instances.append(line)
    return top_instances

def infer_io_ports(instances):
    print(f"🔎 Inferring I/O ports...")
    inputs = set()
    outputs = set()
    for line in instances:
        tokens = line.strip().split()
        pins = [p for p in tokens[1:-1] if p.lower() not in {"vdd", "vss"}]
        n = len(pins)

        if n == 0:
            continue

        if n % 2 == 0:
            num_inputs = num_outputs = n // 2
        else:
            num_inputs = (n + 1) // 2
            num_outputs = n - num_inputs

        for p in pins[:num_inputs]:
            inputs.add(p)
        for p in pins[num_inputs:]:
            outputs.add(p)

    return sorted(inputs), sorted(outputs)

def get_logical_cell_type(devicename, pincount):
    for cell, data in LOGIC_CELLS.items():
        if cell in devicename.lower() and pincount == len(data["ports"]):
            return cell
    return None

def sanitize_name(name):
    return re.sub(r'\W|_', '', name)

def generate_verilog(top_instances, output_path):
    print(f"🛠️ Generating Verilog...")

    verilog = []
    used_cells = set()
    unknown_cells = set()

    inputs, outputs = infer_io_ports(top_instances)

    pin_rename = {}
    for p in inputs:
        pin_rename[p] = f"in{p}"
    for p in outputs:
        pin_rename[p] = f"out{p}"

    raw_name = os.path.splitext(os.path.basename(output_path))[0]
    module_name = sanitize_name(raw_name)  # Remove symbols and underscores
    all_ports = [pin_rename[p] for p in inputs + outputs]
    verilog.append(f"module {module_name} ({', '.join(all_ports)});")

    for p in inputs:
        verilog.append(f"  input wire {pin_rename[p]};")
    for p in outputs:
        verilog.append(f"  output wire {pin_rename[p]};")

    for line in top_instances:
        tokens = line.strip().split()
        if len(tokens) < 3:
            continue
        name = tokens[0]
        raw_pins = [p for p in tokens[1:-1] if p.lower() not in {"vdd", "vss"}]
        mapped_pins = [pin_rename.get(p, p) for p in raw_pins]
        cell_type_raw = tokens[-1].lower()

        if cell_type_raw == "port":
            continue

        logical_cell = get_logical_cell_type(cell_type_raw, len(mapped_pins))

        if logical_cell:
            clean_cell_name = sanitize_name(logical_cell)
            ports = LOGIC_CELLS[logical_cell]["ports"]
            conn = [f".{ports[i]}({mapped_pins[i]})" for i in range(len(mapped_pins))]
            verilog.append(f"  {clean_cell_name} {name} ( {', '.join(conn)} );")
            used_cells.add(logical_cell)
        else:
            ports = [f"pin{i+1}" for i in range(len(mapped_pins))]
            conn = [f".{ports[i]}({mapped_pins[i]})" for i in range(len(mapped_pins))]
            verilog.append(f"  {cell_type_raw} {name} ( {', '.join(conn)} );")
            unknown_cells.add(cell_type_raw)

    verilog.append("endmodule")

    for cell in sorted(unknown_cells):
        verilog.insert(0, f'`include "{cell}.v"')

    for cell in sorted(used_cells):
        defn = LOGIC_CELLS[cell]
        ports = defn["ports"]
        clean_cell_name = sanitize_name(cell)
        verilog.append("")
        verilog.append(f"module {clean_cell_name} ({', '.join(ports)});")
        for p in ports:
            verilog.append(f"  {'output wire' if 'out' in p else 'input wire'} {p};")
        verilog.append(f"  {defn['behavior']}")
        verilog.append("endmodule")

    with open(output_path, "w") as f:
        for line in verilog:
            f.write(line + "\n")

    print(f"✅ Verilog saved to: {output_path}")

def main():
    spice_path = input("📂 Enter full path to your .spice or .cir file: ").strip()
    if not os.path.isfile(spice_path):
        print(f"❌ File not found: {spice_path}")
        return

    top_instances = parse_spice(spice_path)

    basename = os.path.splitext(os.path.basename(spice_path))[0]
    clean_name = re.sub(r'\W|_', '', basename)  # clean file name
    original_dir = os.path.dirname(spice_path)
    dir_basename = os.path.basename(original_dir)
    clean_dirname = re.sub(r'\W|_', '', dir_basename)  # clean directory name

# Construct clean output directory path
    parent_dir = os.path.dirname(original_dir)
    output_dir = os.path.join(parent_dir, clean_dirname)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, clean_name + ".v")


    generate_verilog(top_instances, output_path)

if __name__ == "__main__":
    main()

