#include <iostream>
#include <ostream>
#include <vector>
#include <climits>

class Solution 
{
public:
	int find_kth_element_two_array(std::vector<int>& ns1,std::vector<int>& ns2,int k)
	{
		// [0,pos1] pos1 + 1 element in total
		// [0,pos2] pos2 + 1 element in total
		// pos1 + 1 + pos2 + 1 = k
		// pos2 = k - pos1 - 2
		// -1 <= pos1 <= n - 1
		// -1 <= k - pos1 - 2 <= m - 1
		// k -m - 1 <= pos1 << k - 1
		const int n = ns1.size();
		const int m = ns2.size();
		const int bot = k - m; 
		const int cel = n;

		int low = std::max(0,bot);
		int high = std::min(cel,k);

		int pos1,pos2;

		while(low <= high)
		{
			int mid = (low + high) / 2;
			int count = mid;
			
			int A = (count == 0) ? INT_MIN : ns1[count - 1];
			int C = (k - count == 0) ? INT_MIN : ns2[k - count - 1];
			int B = (count == n) ? INT_MAX : ns1[count];
			int D = (k - count == m) ? INT_MAX : ns2[k - count];
			
			/* ----- A  B ------- */
			/* ----- C  D ------- */

			if((A <= D) && (C <= B))
			{
				pos1 = count - 1;
				pos2 = k - count - 1;
				break;
			}
			else if(A > D)
			{
				high = mid - 1;
			}
			else
			{
				low = mid + 1;
			}
		}
		int ans;
		ans = (pos1 == -1) ? ns2[pos2] : (pos2 == -1) ? ns1[pos1] : std::max(ns1[pos1],ns2[pos2]);
		return ans;
	}

    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) 
	{
		int size1 = nums1.size();
		int size2 = nums2.size();
		if((size1 + size2) % 2)
		{
			// odd numbers in total
			return find_kth_element_two_array(nums1,nums2,(size1 + size2)/2 + 1);
		}
		else
		{ 
			int k1 = find_kth_element_two_array(nums1, nums2,(size1 + size2)/2 );
			int k2 = find_kth_element_two_array(nums1, nums2,(size1 + size2)/2 + 1);
			return (k1 + k2) / 2.0;
		}
    }
};

int main()
{
	Solution sol;
	std::vector<int> ns1,ns2;
	ns1 = {1,3};
	ns2 = {2};
	double test = sol.findMedianSortedArrays(ns1,ns2);
	std::cout << test << std::endl;
		
}
