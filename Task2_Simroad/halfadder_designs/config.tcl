set ::env(DESIGN_NAME) "halfadder"
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/*.v]
set ::env(SDC_FILE) [glob $::env(DESIGN_DIR)/*.sdc]
set ::env(FP_CORE_UTIL) 1
set ::env(PL_TARGET_DENSITY) 0.5