#include <vector>
#include <iostream>
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

void combine_sorted_parts(std::vector<int>& list,int begin,int end)
{
	int mid = (begin + end) / 2;
	std::vector<int> right_part = std::vector<int>(list.begin() + begin,list.begin() + mid + 1);
	std::vector<int> left_part = std::vector<int>(list.begin() + mid + 1,list.begin() + end + 1);
	auto right_iter = right_part.begin();
	auto left_iter = left_part.begin();
	auto iter = list.begin() + begin;
	while (right_iter != right_part.end() && left_iter != left_part.end())
	{
		if(*right_iter <= *left_iter)
		{
			*iter++ = *right_iter++;
		}
		else
		{
			*iter++ = *left_iter++;
		}
	}
	while (right_iter != right_part.end())
	{
		*iter++ = *right_iter++;
	}
	while (left_iter != left_part.end())
	{
		*iter++ = *left_iter++;
	}
}

void merge_sort(std::vector<int>& list,int begin,int end)
{
	if(begin != end)
	{
		int mid = (end + begin) / 2;
		merge_sort(list,begin,mid);
		merge_sort(list,mid+1,end);
		combine_sorted_parts(list,begin,end);
	}
}

int find_majority_element_in_sorted_list(const std::vector<int>& list)
{
	int count = 1;
	int elem = list[0];
	int half_size = list.size() / 2;
	auto iter = list.begin() + 1;
	while(iter != list.end())
	{
		if (count >= half_size)
		{
			return elem;
		}
		else if (elem == *iter)
		{
			count ++;
			iter++;
		}
		else
		{
			elem = *iter++;
			count = 1;
		}
	}
	return -1;
}

int main()
{
	std::vector<int> list = {5,1,1,1,3,4,2,2,2,2};
	merge_sort(list,0,list.size()-1);
	std::cout << find_majority_element_in_sorted_list(list);
}
