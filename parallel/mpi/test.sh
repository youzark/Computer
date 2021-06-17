clear
mpicc ./psrs.c -o test
mpirun -np 4 test
