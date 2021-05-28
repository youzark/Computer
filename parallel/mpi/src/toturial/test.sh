clear
#mpicc psrs.c -o test
#mpirun -np 4 ./test
#mpicc ./send_recv.c -o test
#mpirun -np 2 ./test
#mpicc ./PingPong.c -o test
#mpirun -np 2 ./test
mpicc ./Ring.c -o test
mpirun -np 4 test


