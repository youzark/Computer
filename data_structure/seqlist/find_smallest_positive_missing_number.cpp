#include <iostream>
#include <vector>
#include <cassert>

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

// 0,1,2,3,4,5,6,7,8,9 //bucket sorting strategy
// 1,2,3,4,5,6,7,8,9
// if 1,2,3,4,5,6
//

int main()
{
	std::vector<int> list = { 1,2,3,4,5 };
}
