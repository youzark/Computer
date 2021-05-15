`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: USTC ESLAB 
// Engineer: Wu Yuzhang
// 
// Design Name: RISCV-Pipline CPU
// Module Name: ControlUnit
// Target Devices: Nexys4
// Tool Versions: Vivado 2017.4.1
// Description: RISC-V Instruction Decoder
//////////////////////////////////////////////////////////////////////////////////
//功能和接口说?
    //ControlUnit       是本CPU的指令译码器，组合�?�辑电路
//输入
    // Op               是指令的操作码部�?
    // Fn3              是指令的func3部分
    // Fn7              是指令的func7部分
//输出
    // JalD==1          表示Jal指令到达ID译码阶段
    // JalrD==1         表示Jalr指令到达ID译码阶段
    // RegWriteD        表示ID阶段的指令对应的寄存器写入模�?
    // MemToRegD==1     表示ID阶段的指令需要将data memory读取的�?�写入寄存器,
    // MemWriteD        �?4bit，为1的部分表示有效，对于data memory�?32bit字按byte进行写入,MemWriteD=0001表示只写入最�?1个byte，和xilinx bram的接口类�?
    // LoadNpcD==1      表示将NextPC输出到ResultM
    // RegReadD         表示A1和A2对应的寄存器值是否被使用到了，用于forward的处�?
    // BranchTypeD      表示不同的分支类型，�?有类型定义在Parameters.v�?
    // AluContrlD       表示不同的ALU计算功能，所有类型定义在Parameters.v�?
    // AluSrc2D         表示Alu输入�?2的�?�择
    // AluSrc1D         表示Alu输入�?1的�?�择
    // ImmType          表示指令的立即数格式
//实验要求  
    //补全模块  

`include "Parameters.v"   
module ControlUnit(
    input wire [6:0] Op,
    input wire [2:0] Fn3,
    input wire [6:0] Fn7,
    output wire JalD,
    output wire JalrD,
    output reg [2:0] RegWriteD,
    output wire MemToRegD,
    output reg [3:0] MemWriteD,
    output wire LoadNpcD,
    output reg [1:0] RegReadD,
    output reg [2:0] BranchTypeD,
    output reg [3:0] AluContrlD,
    output wire [1:0] AluSrc2D,
    output wire AluSrc1D,
    output reg [2:0] ImmType        
    ); 
    reg r_JalD;
    reg r_JalrD;
    reg r_MemToRegD;
    reg r_LoadNpcD;
    reg [1:0] r_AluSrc2D;
    reg r_AluSrc1D;
    
    assign JalD = r_JalD;
    assign JalrD = r_JalrD;
    assign MemToRegD = r_MemToRegD;
    assign LoadNpcD = r_LoadNpcD;
    assign AluSrc2D = r_AluSrc2D;
    assign AluSrc1D = r_AluSrc1D;
    
    
    /*
instr_name      opcode     JalD  JalrD  RegWriteD  MemToRegD  MemWriteD  LoadNpcD  RegReadD  BranchTypeD  AluContrlD  AluSrc2D  AluSrc1D  ImmType                             
slli            0010011    0     0      LW         0          0000       0         00        NOBRANCH     SLL         10        1         ITYPE   
srli            0010011    0     0      LW         0          0000       0         00        NOBRANCH     SRL         10        1         ITYPE
srai            0010011    0     0      LW         0          0000       0         00        NOBRANCH     SRA         10        1         ITYPE    

add             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
sub             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
sll             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
srl             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
sra             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
slt             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
sltu            0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
xor             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
or              0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
and             0110011    0     0      LW         0          0000       0         00        000          0000        00        0         000
            0010011    0     0      000        0          0000       0         00        000          0000        00        0         000
            0010011    0     0      000        0          0000       0         00        000          0000        00        0         000
            0010011    0     0      000        0          0000       0         00        000          0000        00        0         000
*/            
    always@(*)
    begin
        {r_JalD,r_JalrD,RegWriteD,r_MemToRegD,MemWriteD,r_LoadNpcD,RegReadD,BranchTypeD,AluContrlD,r_AluSrc2D,r_AluSrc1D,ImmType} = 26'b0;
        case(Op)
            7'b0010011:  //slli,srli,srai,addi ,slti ,sltiu ,xori ,ori ,andi
            begin
                RegWriteD = `LW;
                BranchTypeD = `NOBRANCH;
                case(Fn3)
                    3'b001:
                    begin
                        AluContrlD = `SLL;
                    end
                    3'b101:
                    begin
                        if(Fn7 == 7'b0000000)
                        AluContrlD = `SRL;
                        else
                        AluContrlD = `SRA;
                    end
                    3'b000:
                    AluContrlD = `ADD;
                    3'b010:
                    AluContrlD = `SLT;
                    3'b011:
                    AluContrlD = `SLTU;
                    3'b100:
                    AluContrlD = `XOR;  
                    3'b110:
                    AluContrlD = `OR;
                    3'b111:
                    AluContrlD = `AND;
                endcase
                r_AluSrc2D = 2'b10;
                r_AluSrc1D = 1'b1;
                ImmType = `ITYPE;
            end  //slli,srli,srai,addi ,slti ,sltiu ,xori ,ori ,andi
            7'b0110011:
            begin   
                RegWriteD = `LW;
                BranchTypeD = `NOBRANCH;
                case(Fn3)
                    3'b000:
                    begin
                        if(Fn7 == 7'b0000000)
                        AluContrlD = `ADD;
                        else
                        AluContrlD = `SUB;
                    end
                    3'b001:
                    AluContrlD = `SLL;
                    3'b010:
                    AluContrlD = `SLT;
                    3'b011:
                    AluContrlD = `SLTU;
                    3'b100:
                    AluContrlD = `XOR;
                    3'b101:
                    begin
                        if(Fn7 == 7'b0000000)
                        AluContrlD = `SRL;
                        else
                        AluContrlD = `SRA;
                    end
                    3'b110:
                    AluContrlD = `OR;
                    3'b111:
                    AluContrlD = `AND;
                endcase
                r_AluSrc2D = 2'b00;
                r_AluSrc1D = 1'b1;
                ImmType = `RTYPE;
            end
            7'b0110111: //LUI
            begin
            RegWriteD = `LW;
            BranchTypeD = `NOBRANCH;
            AluContrlD = `LUI;
            r_AluSrc2D = 2'b10;
            r_AluSrc1D = 1'b1;
            ImmType = `UTYPE;
            end // 7'b0110111 LUI
            7'b0010111:
            begin
            RegWriteD = `LW;
            BranchTypeD = `NOBRANCH;
            AluContrlD = `LUI;
            r_AluSrc2D = 2'b10;
            r_AluSrc1D = 1'b0;
            ImmType = `UTYPE;
            end // 7'b0010111 AUIPC 
            7'b1100111:  //JALR
            begin
            r_JalrD = 1'b1;
            RegWriteD = `LW;
            r_LoadNpcD = 1'b1;
            BranchTypeD = `NOBRANCH;
            AluContrlD = `ADD;
            r_AluSrc2D = 2'b01;
            r_AluSrc1D = 1'b0;
            ImmType = `ITYPE;
            end // 7'b1100111  JALR
            7'b1101111:  //JAL
            begin
            r_JalrD = 1'b1;
            RegWriteD = `LW;
            r_LoadNpcD = 1'b1;
            BranchTypeD = `NOBRANCH;
            ImmType = `JTYPE;
            end // 7'b1101111 JAL
            7'b1100011: //BEQ BNE BLT BGE BLTU BGEU
            begin
            case(Fn3)
                3'b000:
                BranchTypeD = `BEQ;
                3'b001:
                BranchTypeD = `BNE;
                3'b100:
                BranchTypeD = `BLT;
                3'b101:
                BranchTypeD = `BGE;
                3'b110:
                BranchTypeD = `BLTU;
                3'b111:
                BranchTypeD = `BGEU;
            endcase //case(Fn3)
            r_AluSrc2D = 2'b00;
            r_AluSrc1D = 1'b1;
            ImmType = `BTYPE;
            end // 7'b1100011 BEQ BNE BLT BGE BLTU BGEU

            7'b0000011: //LB LH LW LBU LHU
            begin
            case(Fn3)
                3'b000:
                RegWriteD = `LB;
                3'b001:
                RegWriteD = `LH;
                3'b010:
                RegWriteD = `LW;
                3'b100:
                RegWriteD = `LBU;
                3'b101:
                RegWriteD = `LHU;
            endcase  //case(Fn3)
            r_MemToRegD = 1'b1;
            AluContrlD = `ADD;
            r_AluSrc2D = 2'b10;
            r_AluSrc1D = 1'b1;
            ImmType = `ITYPE;
            end // 7'b0000011 LB LH LW LBU LHU
            7'b0100011: //SB SH SW
            begin
            case(Fn3)
                3'b000:
                MemWriteD = 4'b0001;
                3'b001:
                MemWriteD = 4'b0011;
                3'b010:
                MemWriteD = 4'b1111;
            endcase //case(Fn3)
            AluContrlD = `ADD;
            r_AluSrc2D = 2'b10;
            r_AluSrc1D = 1'b1;
            ImmType = `STYPE;
            end // 7'b0100011 SB SH SW
        endcase // case(opcode)
    end //always@(*)
endmodule
