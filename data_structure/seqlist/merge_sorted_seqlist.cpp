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
std::vector<int> merge_sorted_list(const std::vector<int>& list1,const std::vector<int>& list2)
{
	int length1 = list1.size();
	int length2 = list2.size();
	int i = 0,j = 0;
	std::vector<int> new_list;
	while(i < length1 && j < length2)
	{
		if(list1[i] <= list2[j])
		{
			new_list.emplace_back(list1[i++]);
		}
		else
		{
			new_list.emplace_back(list2[j++]);
		}
	}
	while(i < length1)
	{
		new_list.emplace_back(list1[i++]);
	}
	while(j < length2)
	{
		new_list.emplace_back(list2[j++]);
	}
	return new_list;
}

int main()
{
	std::vector<int> list1 = {2,31,42,15234};
	std::vector<int> list2 = {1,12,22,32,123,442};
	print_vector(list1);
	print_vector(list2);
	std::vector<int> new_list = merge_sorted_list(list1,list2);
	print_vector(new_list);
}
