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

int median_of_two_sorted_same_size_array(std::vector<int>& list1,std::vector<int>& list2)
{
	int length = list1.size();
	if(length == 1)
	{
		return (list1[0]+ list2[0])/2;
	}
	else if(length == 2)
	{
		if(list2[0] <= list1[0] && list2[1] <= list1[1])
			return (list2[1] + list1[0]) / 2;
		else if(list2[1] <= list1[1])
			return (list2[0] + list2[1]) / 2;
		else if(list2[0] <= list1[0])
			return (list1[0] + list1[1]) / 2;
		else
			return (list2[0] + list1[1]) / 2;
	}
	int mid = length / 2;
	std::cout << "mid :" << mid << std::endl;
	std::cout << "list1 :" << list1[mid] << std::endl;
	print_vector(list1);
	std::cout << "list2 :" << list2[mid] << std::endl;
	print_vector(list2);
	if(list1[mid] == list2[mid])
	{
		return list1[mid];
	}
	else if(list1[mid] < list2[mid])
	{
		/* return median_of_two_sorted_same_size_array(&list1[mid + 1],&list2[mid + 2]) */
		list1 = std::vector<int>(list1.end() - mid - 1,list1.end());
		list2 = std::vector<int>(list2.begin() ,list2.begin() + mid + 1);
		return median_of_two_sorted_same_size_array(list1,list2);
	}
	else
	{
		list2 = std::vector<int>(list2.end() - mid - 1,list2.end());
		list1 = std::vector<int>(list1.begin() ,list1.begin() + mid + 1);
		return median_of_two_sorted_same_size_array(list1,list2);
	}
}

int main()
{
	std::vector<int> list1 = {1,6,8,9,11,345,612};
	std::vector<int> list2 = {4,7,9,21,91,100,104};
	std::cout << median_of_two_sorted_same_size_array(list1,list2);
}
