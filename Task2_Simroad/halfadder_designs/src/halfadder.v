module halfadder (in1, in4, out2, out3);
  input wire in1;
  input wire in4;
  output wire out2;
  output wire out3;
  dxor U2 ( .in1(in1), .in2(in4), .out(out3) );
  dand U3 ( .in1(in1), .in2(in4), .out(out2) );
endmodule

module dand (in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;
  assign out = in1 & in2;
endmodule

module dxor (in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;
  assign out = in1 ^ in2;
endmodule
