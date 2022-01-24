#include <stdio.h>
#include <mpi.h>

#define PING_PONG_LIMIT 10

int main()
{
	MPI_Init(NULL,NULL);

	int worldRank;
	int worldSize;
	MPI_Comm_size(MPI_COMM_WORLD,&worldSize);
	MPI_Comm_rank(MPI_COMM_WORLD,&worldRank);

	int ping_Pong_Count= 0;
	int partner_rank = (worldRank + 1) % 2;
	while(ping_Pong_Count < PING_PONG_LIMIT)
	{
		if(worldRank == ping_Pong_Count%2)
		{
			ping_Pong_Count++;
			MPI_Send(&ping_Pong_Count,1,MPI_INT,partner_rank,0,MPI_COMM_WORLD);
			printf("%d sent ping_Pong_Count %d to %d\n",worldRank,ping_Pong_Count,partner_rank);
		}
		else
		{
			MPI_Recv(&ping_Pong_Count,1,MPI_INT,partner_rank,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			printf("%d receive ping_Pong_Count %d from %d\n",worldRank,ping_Pong_Count,partner_rank);
		}
	}
	MPI_Finalize();
}
