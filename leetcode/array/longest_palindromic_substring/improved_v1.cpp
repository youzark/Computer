#include <iostream>
#include <string>

// too many hard-coded constants which make it easy to beark edge case
class Solution {
public:
    std::string longestPalindrome(std::string s) 
	{
		int iter_max = 0 , start = -1;
		int length = s.length();
		for(int iter = 0 ; iter < length; iter++)
		{
			int local_max = 0,local_start = -1;
			for(int i = 0;i < length - iter ;i++)
			{
				int seq_index = i;
				int rev_index = length - 1 - iter - i;
				std::cout << "iter: " << iter << " i: " << i ;
				std::cout << " seq: " << seq_index << " rev: " ;
				std::cout << " s[seq_index]: " << s[seq_index] ;
				std::cout << " s[rev_index]: " << s[rev_index] << std::endl;
				if(s[seq_index] == s[rev_index])
				{
					local_max++;
				}
				else
				{
					if(local_max > iter_max)
					{
						iter_max = local_max;
						start = local_start;
					}
					local_max = 0;
					local_start = i+1;
				}
			}
			if(local_max > iter_max)
			{
				iter_max = local_max;
				if(local_start == -1)
				{
					start = local_start + 1;
				}
				else
				{
					start = local_start;
				}
			}
			std::cout  << "iter_max: " << iter_max << " start: " << start << std::endl;
		}
		return s.substr(start, iter_max);
    }
};

int main()
{
	std::string test_string = "abb";
	Solution test;
	std::cout << test.longestPalindrome(test_string) << std::endl;;
	return 0;
}
