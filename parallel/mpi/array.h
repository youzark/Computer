void arrayCp(int arr1[],int arr2[],int start,int end)
{
	int i = start;
	while(i <= end)
	{
		arr1[i] = arr2[i];
		i++;
	}
}
