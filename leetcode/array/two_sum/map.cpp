#include <iostream>
#include <map>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
	{
		map<int, int>mp_exist,mp_pos;
		vector<int>result = {0,0};
		for(int i=0;i < nums.size();i++)
		{
			if(mp_exist[target-nums[i]]==1 && mp_pos[target-nums[i]]!=i)
			{
				result = {mp_pos[target - nums[i]],i};
				return result;
			}
			else 
			{
				mp_exist[nums[i]] = 1;
			}
			mp_pos[nums[i]] = i;
		}
		return result;
	}
};

int main()
{
	class Solution so;

}
