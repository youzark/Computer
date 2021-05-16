#include <stdio.h>
#include <omp.h>
#include "../include/array.h"
#include "../include/MergeSort.h"

#define num_thread 5

void psrs(int arr[],int start,int end)
{
	int step;
	int i,j = 0,k;
	int sample[num_thread* num_thread];
	int pivot[num_thread - 1];
	int partition[num_thread][num_thread][1000];  // count[No. processor][No. partition][inside partition]
	int count[num_thread][num_thread] = {0}; // count[No. processor][No. partition]
	
	step = (end - start + 1) / num_thread;

	omp_set_num_threads(num_thread);
#pragma omp parallel 
	{
		int id;
		id = omp_get_thread_num();
		mergeSort(arr,start + id * step,start + (id + 1)* step - 1);
		
#pragma omp critical
		for(int l = 0;l < num_thread;l++)
		{
			sample[j++] = arr[start + id*step + l*step/(num_thread)];
		}
#pragma omp barrier
#pragma omp master
		{
			mergeSort(sample,0,num_thread*num_thread-1);
		//printf("sample:");
		//printArray(sample,0,24);
			for(k = 0;k < num_thread - 1;k++)
			{
				pivot[k] = sample[(k + 1) * num_thread];
			}
		//printf("pivot:");
		//printArray(pivot,0,3);
		}
#pragma omp barrier
		for(int l = 0;l < step;l ++) // offset from start + id*step, traverse all elems of id's processor
		{
			for(int p = 0 ;p < num_thread;p++)  //the p.th partition
			{
	//			printf("id:%d part:%d num:%d l:%d \n",id,p,arr[start + id*step + l],l);
				if(arr[start + id*step + l] < pivot[p])
				{
					partition[id][p][count[id][p]++] = arr[start + id*step + l];
					break;
				}
				else if(p == num_thread - 1)
				{
					partition[id][p][count[id][p]++] = arr[start + id*step + l];
				}
			}
		}
		/*
#pragma omp master
		{
			for(int t = 0 ;t < num_thread;t ++)
			{
				printf("processor:%d\n",t);
				for(int l = 0;l < num_thread;l ++)
				{
					printf("part:%d  ",l);
					printf("count:%d  ",count[t][l]);
					printArray(partition[t][l],0,count[t][l]-1);
				}
			}
		}
		*/
	}

#pragma omp parallel
	{
		int id = omp_get_thread_num();
		for(int l = 0;l < num_thread;l++) // the id.th processor will copy id'th part from l's precessor other than id itself
		{
			if(l != id)
			{
				arrayCp(partition[id][id] + count[id][id],partition[l][id],0,count[l][id]-1);
				count[id][id] += count[l][id];
			}
		}
		mergeSort(partition[id][id],0,count[id][id] - 1);
	}
	for(k = 0;k < num_thread;k ++)
	{
		printArray(partition[k][k],0,count[k][k] - 1);
	}
	printf("\n");
}

int main()
{
	int arr[50] = {40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,50,49,48,47,46,45,44,43,42,41};
	psrs(arr,0,49);
	return 0;
}
