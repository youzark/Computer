#include <stdio.h>
#include <mpi.h>

int main()
{
	MPI_Init(NULL,NULL);

	int worldSize;
	MPI_Comm_size(MPI_COMM_WORLD,&worldSize);

	int worldRank;
	MPI_Comm_rank(MPI_COMM_WORLD,&worldRank);

	printf("Hello world from processor %d out of %d processors \n",worldRank,worldSize);

	MPI_Finalize();
}



