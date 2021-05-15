iverilog -o test *.v ./BRAMModule/*.v
./test
gnome-terminal -e 'gtkwave test.vcd'
