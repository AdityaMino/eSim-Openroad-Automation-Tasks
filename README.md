
# 🔄 eSim to OpenROAD Automation Toolkit

This repository contains two automation scripts and all related resources for:
- 🧠 **Converting SPICE Netlists (from eSim) to Synthesizable Verilog**
- 🏭 **Running an End-to-End RTL-to-GDSII Flow using OpenROAD via OpenLane**

---

## 📑 Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Project Structure](#project-structure)
- [Installation Instructions](#installation-instructions)
- [Script 1: spice_to_verilog.py](#script-1-spice_to_verilogpy)
- [Script 2: simroad.py](#script-2-simroadpy)
- [Errors Encountered & Fixes](#-errors-encountered--solutions)
- [Results](#results)
- [Conclusion](#conclusion)
- [Acknowledgements](#acknowledgements)

---

## 🧠 Introduction

In VLSI design, moving from transistor-level descriptions (like SPICE) to higher abstraction levels (like Verilog) is critical for automating digital design and enabling large-scale synthesis. This project builds a fully open-source and automated flow from circuit creation in **eSim** to **layout generation in OpenROAD** using **OpenLane**. The approach aims to minimize human intervention while accelerating prototyping and research for academia and hobbyists alike.

---

## 🎯 Objectives

- Convert eSim-generated SPICE netlists into synthesizable Verilog files.
- Automate the OpenLane flow to synthesize, place, and route those Verilog files.
- Provide reproducible scripts, circuit files, and logs for demonstration.

---

## 📁 Project Structure

```bash
├── spice_to_verilog.py         # Script 1: Netlist to Verilog
├── simroad.py                  # Script 2: OpenLane flow automation
├── sample_circuits/
│   └── half_adder.cir
├── outputs/
│   └── final.gds
├── eSim_Installation_Instructions.md
├── README.md
```

---

## 🛠️ Installation Instructions

👉 See [eSim Installation Instructions](eSim_Installation_Instructions.md) for full OS-wise setup.

---

## ⚙️ Script 1: `spice_to_verilog.py`

This Python script:
- Parses a SPICE netlist exported from eSim.
- Maps NMOS/PMOS arrangements into logic gates.
- Wraps logic into a Verilog `module`.
- Handles node parsing, port identification, and syntax generation.

Run it:
```bash
python3 spice_to_verilog.py half_adder.cir > half_adder.v
```

---

## 🚀 Script 2: `simroad.py`

The script automates:
1. Prompting user for OpenLane path.
2. Creating design workspace in `OpenLane/design/`.
3. Copying Verilog file and generating `config.tcl`.
4. Running OpenLane via `subprocess`:
   ```bash
   ./flow.tcl -design esim_design
   ```
5. Collecting output `.gds`, `.def`, logs to local `outputs/`.
6. Displaying colored terminal messages with emojis.

---

## 🧩 Errors Encountered & Solutions

| Issue | Description | Resolution |
|-------|-------------|------------|
| **Missing "Convert to Verilog" in eSim GUI** | Option was unclear or missing | Used manual netlist and wrote our own parser |
| **KLayout launch failed** | GUI not supported on headless systems | Printed step-by-step viewing instructions |
| **Hardcoded OpenLane path** | Not portable across machines | Used dynamic `input()` + `Path.resolve()` |
| **File not found errors** | Static assumptions on folders | Used `os.makedirs()` and verified paths |
| **Output clutter** | Poor readability in terminal | Added spacing, emojis, and color-coded logs |
| **No clean Verilog structure** | eSim exports were not clean modules | Manually wrapped into syntactically correct modules |

---

## 🖼️ Results

- ✅ **Successfully converted SPICE to Verilog**
- ✅ **Successfully generated GDS using OpenLane**
- ✅ **Verified layout using KLayout manually**
- 📸 All screenshots and logs available in `outputs/`

---

## 🔚 Conclusion

This repository demonstrates a powerful and reproducible open-source VLSI automation pipeline—starting from **schematic design in eSim**, **netlist parsing**, **Verilog generation**, and culminating in **layout creation using OpenROAD**. It serves as an educational and prototyping tool for students and researchers in digital VLSI design.

---

## 🙌 Acknowledgements

- [FOSSEE IIT Bombay](https://esim.fossee.in) for eSim development.
- [The OpenROAD Project](https://theopenroadproject.org/) and [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane) for EDA tools.
- [KLayout](https://www.klayout.de/) for viewing GDS files.
