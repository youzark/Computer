#include <vector>
#include <string>
class Solution {
public:
    int lengthOfLongestSubstring(std::string s) 
	{
		// init dict to all -1(init start pos)
		// if the current scanning substring contain char'a' then 
		// dict['a'] will record the pos where 'a' is find
		// dict['a'] < start indicate 'a' not appear in the current substring
		// length = i - start
		// start is the last bit of former substring
		std::vector<int> dict(256,-1);
		int maxlength = 0,start = -1;
		for(int i = 0; i != s.length();i++)
		{
			// reset start
			if(dict[s[i]] > start)
			{
				// where to reset start position
				// at least you can set it to start + 1
				// dict[s[i]] is better cause dict[s[i]] will conflict with i 
				// and thus give a definately shorter string
				start = dict[s[i]];
			}
			// record s[i]
			dict[s[i]] = i;
			// reset maxlength
			maxlength = std::max(maxlength,i - start);
		}
		return maxlength;
    }
};
