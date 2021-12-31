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

void shift_m_elements_right(std::vector<int>& list,int m)
{
	std::vector<int> temp_list;
	int cur = 0;
	for(;cur < m ;cur++)
	{
		temp_list.push_back(list[cur]);
	}
	for(;cur < list.size();cur++)
	{
		list[cur - m] = list[cur];
	}
	for(int back_iter = 1;back_iter <= m;back_iter++)
	{
		list[cur - back_iter] = temp_list[m - back_iter];
	}
}

int main()
{
	std::vector<int> list = {1,2,3,4,5,6,7,8};
	print_vector(list);
	shift_m_elements_right(list,5);
	print_vector(list);
}
