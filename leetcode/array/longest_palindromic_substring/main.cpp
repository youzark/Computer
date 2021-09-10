#include <typeinfo>
#include <iostream>
#include <string>
#include <stack>

class Solution {
public:
    std::string longestPalindrome(std::string s) 
	{
		int i=0,j;
		int length = s.length();
		int max = 1,start = 0,end = 0;
		for(i = 0 ;i < length; i++)
		{
			for(j = i + max ;j < length ;j++)
			{
				if(is_palindrome(i,j,s))
				{
					start = i;
					end = j;
					max = j - i + 1;
				}
			}
		}
		return s.substr(start,end - start + 1);
    }

	bool is_palindrome(int start,int end,std::string s)
	{
		std::stack<char> reverse_string;
		bool is_palindrome = true;
		for(int i = start; i <= end ; i++)
		{
			reverse_string.push(s[i]);
		}
		for(int i = start; i <= end ;i ++)
		{
			is_palindrome = is_palindrome & (reverse_string.top() == s[i]);
			reverse_string.pop();
		}
		return is_palindrome;
	}
};

int main()
{
	Solution test;
	std::string test_string = "qwerrewqs";
	std::cout << test_string.substr(2,3) << std::endl;
	std::cout << test.longestPalindrome(test_string) << std::endl;
	return 0;
}
