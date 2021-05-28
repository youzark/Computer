#include <stdio.h>
#include <mpi.h>

int main()
{
	MPI_Init(NULL,NULL);

	int worldSize;
	MPI_Comm_size(MPI_COMM_WORLD,&worldSize);
	
	int worldRank;
	MPI_Comm_rank(MPI_COMM_WORLD,&worldRank);

	int number;
	if(worldRank == 0)
	{
		number = -1;
		MPI_Send(&number,1,MPI_INT,1,0,MPI_COMM_WORLD);
	}
	else if(worldRank == 1)
	{
		MPI_Recv(&number,1,MPI_INT,0,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
		printf("Process 1 receive number %d from Process 0\n",number);
	}
	MPI_Finalize();

}
