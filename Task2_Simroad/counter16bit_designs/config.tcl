set ::env(DESIGN_NAME) "counter16bit"
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/*.v]
set ::env(SDC_FILE) [glob $::env(DESIGN_DIR)/*.sdc]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(FP_CORE_UTIL) 1
set ::env(PL_TARGET_DENSITY) 0.5