iverilog -g2012 -s ./cache_tb.sv -o test -c ./file_list.txt
./test
gnome-terminal -e 'gtkwave test.vcd'

