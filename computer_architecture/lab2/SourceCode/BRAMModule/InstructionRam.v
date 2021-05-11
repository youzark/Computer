`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: USTC ESLAB 
// Engineer: Wu Yuzhang
// 
// Design Name: RISCV-Pipline CPU
// Module Name: InstructionRamWrapper
// Target Devices: Nexys4
// Tool Versions: Vivado 2017.4.1
// Description: a Verilog-based ram which can be systhesis as BRAM
// 
//////////////////////////////////////////////////////////////////////////////////
//功能说明
    //同步读写bram，a口只读，用于取指，b口可读写，用于外接debug_module进行读写
    //写使能为1bit，不支持byte write
//输入
    //clk               输入时钟
    //addra             a口读地址
    //addrb             b口读写地址
    //dinb              b口写输入数据
    //web               b口写使能
//输出
    //douta             a口读数据
    //doutb             b口读数据
//实验要求  
    //无需修改

module InstructionRam(
    input  clk,
    input  web,
    input  [31:2] addra, addrb,
    input  [31:0] dinb,
    output reg [31:0] douta, doutb
);
initial begin douta=0; doutb=0; end

wire addra_valid = ( addra[31:14]==18'h0 );
wire addrb_valid = ( addrb[31:14]==18'h0 );
wire [11:0] addral = addra[13:2];
wire [11:0] addrbl = addrb[13:2];

reg [31:0] ram_cell [0:4095];

initial begin    // 可以把测试指令手动输入此处
    ram_cell[0] = 32'h00000537;
    ram_cell[1] = 32'h00000000;
    ram_cell[2] = 32'h00000000;
    ram_cell[3] = 32'h00000000;
    ram_cell[4] = 32'h00000000;
    ram_cell[5] = 32'h40050113;
    ram_cell[6] = 32'h00000000;
    ram_cell[7] = 32'h00000000;
    ram_cell[8] = 32'h00000000;
    ram_cell[9] = 32'h00000000;
    ram_cell[10] = 32'h00806293;
    ram_cell[11] = 32'h00000000;
    ram_cell[12] = 32'h00000000;
    ram_cell[13] = 32'h00000000;
    ram_cell[14] = 32'h00000000;
    ram_cell[15] = 32'h00c000ef;
    ram_cell[16] = 32'h00000000;
    ram_cell[17] = 32'h00000000;
    ram_cell[18] = 32'h00000000;
    ram_cell[19] = 32'h00000000;
    ram_cell[20] = 32'h00652023;
    ram_cell[21] = 32'h00000000;
    ram_cell[22] = 32'h00000000;
    ram_cell[23] = 32'h00000000;
    ram_cell[24] = 32'h00000000;
    ram_cell[25] = 32'h0000006f;
    ram_cell[26] = 32'h00000000;
    ram_cell[27] = 32'h00000000;
    ram_cell[28] = 32'h00000000;
    ram_cell[29] = 32'h00000000;
    ram_cell[30] = 32'h00306e93;
    ram_cell[31] = 32'h00000000;
    ram_cell[32] = 32'h00000000;
    ram_cell[33] = 32'h00000000;
    ram_cell[34] = 32'h00000000;
    ram_cell[35] = 32'h01d2f663;
    ram_cell[36] = 32'h00000000;
    ram_cell[37] = 32'h00000000;
    ram_cell[38] = 32'h00000000;
    ram_cell[39] = 32'h00000000;
    ram_cell[40] = 32'h0002e313;
    ram_cell[41] = 32'h00000000;
    ram_cell[42] = 32'h00000000;
    ram_cell[43] = 32'h00000000;
    ram_cell[44] = 32'h00000000;
    ram_cell[45] = 32'h00008067;
    ram_cell[46] = 32'h00000000;
    ram_cell[47] = 32'h00000000;
    ram_cell[48] = 32'h00000000;
    ram_cell[49] = 32'h00000000;
    ram_cell[50] = 32'hfff28293;
    ram_cell[51] = 32'h00000000;
    ram_cell[52] = 32'h00000000;
    ram_cell[53] = 32'h00000000;
    ram_cell[54] = 32'h00000000;
    ram_cell[55] = 32'hffc10113;
    ram_cell[56] = 32'h00000000;
    ram_cell[57] = 32'h00000000;
    ram_cell[58] = 32'h00000000;
    ram_cell[59] = 32'h00000000;
    ram_cell[60] = 32'h00112023;
    ram_cell[61] = 32'h00000000;
    ram_cell[62] = 32'h00000000;
    ram_cell[63] = 32'h00000000;
    ram_cell[64] = 32'h00000000;
    ram_cell[65] = 32'hffc10113;
    ram_cell[66] = 32'h00000000;
    ram_cell[67] = 32'h00000000;
    ram_cell[68] = 32'h00000000;
    ram_cell[69] = 32'h00000000;
    ram_cell[70] = 32'h00512023;
    ram_cell[71] = 32'h00000000;
    ram_cell[72] = 32'h00000000;
    ram_cell[73] = 32'h00000000;
    ram_cell[74] = 32'h00000000;
    ram_cell[75] = 32'hfddff0ef;
    ram_cell[76] = 32'h00000000;
    ram_cell[77] = 32'h00000000;
    ram_cell[78] = 32'h00000000;
    ram_cell[79] = 32'h00000000;
    ram_cell[80] = 32'h00012283;
    ram_cell[81] = 32'h00000000;
    ram_cell[82] = 32'h00000000;
    ram_cell[83] = 32'h00000000;
    ram_cell[84] = 32'h00000000;
    ram_cell[85] = 32'hfff28293;
    ram_cell[86] = 32'h00000000;
    ram_cell[87] = 32'h00000000;
    ram_cell[88] = 32'h00000000;
    ram_cell[89] = 32'h00000000;
    ram_cell[90] = 32'h00612023;
    ram_cell[91] = 32'h00000000;
    ram_cell[92] = 32'h00000000;
    ram_cell[93] = 32'h00000000;
    ram_cell[94] = 32'h00000000;
    ram_cell[95] = 32'hfcdff0ef;
    ram_cell[96] = 32'h00000000;
    ram_cell[97] = 32'h00000000;
    ram_cell[98] = 32'h00000000;
    ram_cell[99] = 32'h00000000;
    ram_cell[100] = 32'h00012383;
    ram_cell[101] = 32'h00000000;
    ram_cell[102] = 32'h00000000;
    ram_cell[103] = 32'h00000000;
    ram_cell[104] = 32'h00000000;
    ram_cell[105] = 32'h00410113;
    ram_cell[106] = 32'h00000000;
    ram_cell[107] = 32'h00000000;
    ram_cell[108] = 32'h00000000;
    ram_cell[109] = 32'h00000000;
    ram_cell[110] = 32'h00730333;
    ram_cell[111] = 32'h00000000;
    ram_cell[112] = 32'h00000000;
    ram_cell[113] = 32'h00000000;
    ram_cell[114] = 32'h00000000;
    ram_cell[115] = 32'h00012083;
    ram_cell[116] = 32'h00000000;
    ram_cell[117] = 32'h00000000;
    ram_cell[118] = 32'h00000000;
    ram_cell[119] = 32'h00000000;
    ram_cell[120] = 32'h00410113;
    ram_cell[121] = 32'h00000000;
    ram_cell[122] = 32'h00000000;
    ram_cell[123] = 32'h00000000;
    ram_cell[124] = 32'h00000000;
    ram_cell[125] = 32'h00008067;
    ram_cell[126] = 32'h00000000;
    ram_cell[127] = 32'h00000000;
    ram_cell[128] = 32'h00000000;
    ram_cell[129] = 32'h00000000;
end

always @ (posedge clk)
    douta <= addra_valid ? ram_cell[addral] : 0;
    
always @ (posedge clk)
    doutb <= addrb_valid ? ram_cell[addrbl] : 0;

always @ (posedge clk)
    if(web & addrb_valid) 
        ram_cell[addrbl] <= dinb;

endmodule

