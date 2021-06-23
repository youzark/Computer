#include <stdio.h>
void merge(int arr[],int start,int mid,int end)
{
	int i,j,k;
	int n1 = mid - start + 1;
	int n2 = end - mid;

	int left[n1] ,right[n2];

	for(i = 0; i < n1; i++)
	{
		left[i] = arr[start + i];
	}
	for(j = 0; j < n2; j++)
	{
		right[j] = arr[j + mid + 1];
	}

	i = 0;
	j = 0;
	k = start;

	while(i < n1 && j < n2)
	{
		if(left[i] <= right[j])
		{
			arr[k++] = left[i++];
		}
		else
		{
			arr[k++] = right[j++];
		}
	}
	
	while(i < n1)
	{
		arr[k++] = left[i++];
	}

	while(j < n2)
	{
		arr[k++] = right[j++];
	}
}

void merge_sort(int arr[],int start,int end)
{
	if(start < end)
	{
		int mid = (start + end) / 2;

		merge_sort(arr,start,mid);
		merge_sort(arr,mid+1,end);

		merge(arr,start,mid,end);
	}
}



void print_array(int arr[],int start,int end)
{
	int i = start;
	printf("%d",arr[i++]);
	while(i <= end)
	{
		printf(",%d",arr[i++]);
	}
	printf("\n");
}






