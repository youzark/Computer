#include <iostream>
#include <string>
#include <vector>
#include <functional>
#include <algorithm>

// a way to create anonymous function
// treat function like a variable

// when to use it?
// whenever you have a function pointer
// just a simple way for us to define a function and use a like a variable



void for_each(const std::vector<int>& nums,const std::function<void(int)>& func)
{
	for (int num : nums) 
	{
		func(num);
	}
}

int main()
{
	std::vector<int> nums = {1,2,34,5,612,12};
	std::string message = "Greet from Main function";

	// [] captures variable in caller function and pass to callee
	// [&] captures all vars by reference
	// [=] captures all vars by value
	// [&var_name]
	// [var_name] by value
	std::cout << "test1:basic usage and capture" << std::endl;
	auto lambda = [&message](int value)
	{ 
		std::cout << "value: " << value; 
		std::cout << " external message:" << message << std::endl; 
	};
	for_each(nums, lambda);
	std::cout << std::endl;


	std::cout << "test2:one common usage:find_if function" << std::endl;
	// one usage: find_value
	int comp = 10;
	auto predicate = [&comp](int value)
	{
		return value > comp;
	};
	auto iter = std::find_if(nums.begin(),nums.end(), predicate);
	std::cout << "result value: " << *iter << " ,it is the first bigger than :" << comp << std::endl;


	return 0;
}
