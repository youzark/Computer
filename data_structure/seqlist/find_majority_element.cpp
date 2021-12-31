#include <vector>
#include <iostream>

class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
		int count = 0 , majority_element;
		for(auto iter = nums.begin();iter != nums.end();iter ++)
		{
			if(count == 0)
			{
				majority_element = *iter;
				count++;
			}
			else if(majority_element == *iter)
			{
				count ++;
			}
			else
			{
				count --;
			}
		}
		return majority_element;
    }

};
