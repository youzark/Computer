#include <iostream>
#include <vector>

void print_vector(const std::vector<int>& list)
{
	std::cout << "**********************************" << std::endl;
	for(auto elem : list)
	{
		std::cout << elem << " ";
	}
	std::cout << std::endl;
	std::cout << "**********************************" << std::endl;
	std::cout << std::endl;
}

int find_x_pos(int x,int start,int end,const std::vector<int>& list)
{
	if(start == end)
		return start;
	int mid = (end + start) / 2;
	if (list[mid] == x)
	{
		return mid;
	}
	else if (x < list[mid])
	{
		return find_x_pos(x,start,mid-1,list);
	}
	else
	{
		return find_x_pos(x,mid + 1,end,list);
	}
}

int main()
{
	std::vector<int> list = {1,2,3,4,5,6,7,8};
	print_vector(list);
}
