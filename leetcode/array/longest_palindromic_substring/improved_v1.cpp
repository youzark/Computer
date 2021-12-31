#include <algorithm>
#include <iostream>
#include <string>

// too many hard-coded constants which make it easy to beark edge case
class Solution {
public:
	int lower_bound(int iter)
	{
		return iter < 0 ? 0 : iter;
	}
	int upper_bound(int iter,int length)
	{
		return iter < 0 ? iter + length - 1 : length - 1;
	}
    std::string longestPalindrome(std::string s) 
	{
		std::string reverse_string = s;
		reverse(reverse_string.begin(), reverse_string.end());
		int length = s.length();
		int iter = -(length - 1);
		int iter_max = 0,iter_start;
		for(;iter <= (length - 1);iter++)
		{
			int sequential_begin = lower_bound(iter);
			int sequential_end = upper_bound(iter,length);
			int local_length = sequential_end - sequential_begin + 1;
			int reverse_begin = length - 1 - sequential_end;
			std::cout << "sequential_begin: " << sequential_begin << " sequential_end: " << sequential_end << std::endl;
			int local_max = 0,local_start = sequential_begin;
		}
    }
};

int main()
{
	std::string test_string = "aacabdkacaa";
	Solution test;
	std::cout << test.longestPalindrome(test_string) << std::endl;;
	return 0;
}
