iverilog -o test *.v ./BRAMModule/*.v
./test
gtkwave test.vcd
