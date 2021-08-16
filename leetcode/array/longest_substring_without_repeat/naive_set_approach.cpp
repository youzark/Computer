#include <string>
#include <set>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) 
	{
		std::set<char> myset;
		int last_end = -1;
		int maxlength = 0;
		// myset contain s[last_end + 1,i]
		for (int i = 0; i < s.length(); ++i)
		{
			// reset last end
			// erase all elem until confict one is removed
			if(myset.count(s[i]) != 0)
			{
				while(myset.count(s[i]) != 0)
				{
					last_end++;
					myset.erase(s[last_end]);
				}
			}
			myset.insert(s[i]);
			maxlength = std::max(maxlength, i - last_end);
		}
		return maxlength;
    }
};

int main()
{
	Solution test;
	std::string test_case1("whynottryagain");
	return 0;
}
