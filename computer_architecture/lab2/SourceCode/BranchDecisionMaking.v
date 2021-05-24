`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: USTC ESLAB 
// Engineer: Wu Yuzhang
// 
// Design Name: RISCV-Pipline CPU
// Module Name: BranchDecisionMaking
// Target Devices: Nexys4
// Tool Versions: Vivado 2017.4.1
// Description: Decide whether to branch 
//////////////////////////////////////////////////////////////////////////////////
//功能和接口说�?
    //BranchDecisionMaking接受两个操作数，根据BranchTypeE的不同，进行不同的判断，当分支应该taken时，令BranchE=1'b1
    //BranchTypeE的类型定义在Parameters.v�?
//推荐格式�?
    //case()
    //    `BEQ: ???
    //      .......
    //    default:                            BranchE<=1'b0;  //NOBRANCH
    //endcase
//实验要求  
    //补全模块
 
`include "Parameters.v"   
module BranchDecisionMaking(
    input wire [2:0] BranchTypeE,
    input wire [31:0] Operand1,Operand2,
    output reg BranchE
    );
	
	always@(*)
	begin
		BranchE = 1'b0;
    	case(BranchTypeE)
	    	`NOBRANCH:
	    	begin
	    	end
    		`BEQ:
			begin
				if(Operand1 == Operand2)
					BranchE = 1'b1;
			end
    		`BNE:
			begin
				if(Operand1 != Operand2)
					BranchE = 1'b1;
			end
    		`BLT:
			begin
				if($signed(Operand1) < $signed(Operand2))
					BranchE = 1'b1;
			end
    		`BLTU:
			begin
				if(Operand1 < Operand2)
					BranchE = 1'b1;
			end
    		`BGE:
			begin
				if($signed(Operand1) >= $signed(Operand2))
					BranchE = 1'b1;
			end
    		`BGEU:	  
			begin
				if(Operand1 >= Operand2)
					BranchE = 1'b1;
			end
    	endcase
	end
endmodule

