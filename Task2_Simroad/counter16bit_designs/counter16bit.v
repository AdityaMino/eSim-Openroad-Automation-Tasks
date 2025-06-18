// counter_16bit.v
module counter16bit (
    input  wire clk,       // Clock input
    input  wire rst,       // Active-high synchronous reset
    output reg [15:0] count // 16-bit counter output
);

    always @(posedge clk) begin
        if (rst)
            count <= 16'b0;        // Reset counter to 0
        else
            count <= count + 1;    // Increment counter
    end

endmodule

