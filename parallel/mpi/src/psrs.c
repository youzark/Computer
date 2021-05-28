#include <stdio.h>
#include <mpi.h>
#include <stdlib.h>
#include <string.h>
#include "../include/MergeSort.h"


void psrs(int *arr,int start,int end,int id,int world_size)
{
	int step = (end - start + 1)/world_size;

	int *global_sample;
	if(id == 0)
	{
		global_sample = (int*)malloc(world_size*world_size*sizeof(int));
		memset(global_sample,0,world_size*world_size*sizeof(int));
	}

	int *sample;
	sample = (int*)malloc(world_size*sizeof(int));
	memset(sample,0,world_size*sizeof(int));

	int *pivot;
	pivot = (int*)malloc((world_size-1)*sizeof(int));
	memset(pivot,0,(world_size-1)*sizeof(int));

	merge_sort(arr,start + id * step,start + (id+1)*step - 1);

	for(int l = 0;l < world_size;l++)
	{
		sample[l] = arr[start + id*step + l*step/world_size];
	}
	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Gather(sample,world_size,MPI_INT,global_sample,world_size,MPI_INT,0,MPI_COMM_WORLD);

	if(id == 0)
	{
		merge_sort(global_sample,0,world_size*world_size - 1);
		for(int k ;k < world_size - 1;k++)
		{
			pivot[k] = global_sample[(k+1)*world_size];
		}
	}

	MPI_Bcast(pivot,world_size-1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Barrier(MPI_COMM_WORLD);

	int partition[world_size][world_size][1000];
	int **count;
	count = (int**)malloc(world_size * sizeof(int*));
	for(int i = 0 ;i < world_size;i++)
	{
		count[i] = (int*)calloc(world_size,sizeof(int));
	}
	
	for(int l = 0;l < step;l++)
	{
		for(int p = 0 ;p < world_size;p++)
		{
			if(arr[start + id*step + l ] < pivot[p])
			{
				partition[id][p][count[id][p]++] = arr[start + id*step + l];
				break;
			}
			else if(p == world_size - 1)
			{
				partition[id][p][count[id][p]++] = arr[start + id*step + l];
			}
		}
	}

	/*
	int **partition;
	partition = (int**)malloc(world_size*sizeof(int*));
	for(int i ;i < world_size;i++)
	{
		partition[i] = (int*)calloc(world_size,sizeof(int));
	}
	int *count;
	count = (int*)calloc(world_size,sizeof(int));

	for(int l = 0 ;l < step;l++)
	{
		for(int p = 0;p < world_size;p++)
		{
			if(arr[start + id*step + l] < pivot[p])
			{
				partition[p][count[p]++] = arr[start + id*step + l];
				break;
			}
			else if(p == world_size -1)
			{
				partition[p][count[p]++] = arr[start + id*step + l];
			}
		}
	}

	for(int i = 0;i < world_size;i++)
	{
		MPI_Alltoallc(partition)
	}
	int *sent_count;
	sent_count = (int*)calloc(world_size,sizeof(int));
	int *sent_disp;
	sent_disp = (int*)calloc(world_size,sizeof(int));
	int *recv_count;
	recv_count = (int*)calloc(world_size,sizeof(int));
	int *recv_disp;
	recv_disp = (int*)calloc(world_size,sizeof(int));
	*/


	


}

int main()
{
	MPI_Init(NULL,NULL);
	int world_size,rank;
	MPI_Comm_size(MPI_COMM_WORLD,&world_size);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	int arr[50] = {40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,50,49,48,47,46,45,44,43,42,41};
	printf("test\n");
	psrs(arr,0,49,rank,world_size);
	MPI_Finalize();
}
