`timescale 1ns/1ns

module test;

reg rst;
reg clk;
initial 
begin
	rst = 1;
	clk = 1;
	#5 rst = 0;
	repeat(100)
   	#20 clk = ~clk;
	$finish;
end

initial 
begin
	$dumpfile("test.vcd");
	$dumpvars(0,test);
end

RV32Core CPU1
(
    .CPU_CLK(clk),
    .CPU_RST(rst)
);

endmodule

