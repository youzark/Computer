#include <string>
class Solution {
public:
	std::string longestPalindrome(std::string s) {
		int start = 0;
		int length = s.length();
		int end = 0;
		int maxlength=1;
		for(int i = 0;i < length;i++) {
			for(int j = i + maxlength - 1; j < length; j++) {
				if(isPalindorme(s,i,j)) {
					start = i;
					end = j;
					maxlength = j - i + 1;
				}
			}
		}
		return s.substr(start,end-start + 1);
    }
	bool isPalindorme(std::string& s,int start,int end) {
		bool isPal = 1;
		while(start <= end) {
			if(s[start] != s[end]) {
				isPal = 0;
				break;
			}
			start++;
			end--;
		}
		return isPal;
	}
};
