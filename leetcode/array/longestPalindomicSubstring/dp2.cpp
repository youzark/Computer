#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
		int start = 0;
		int maxLength = 1;
		int length = s.length();

		if(length == 1) {
			return s;
		}

		std::vector<std::vector<bool>> memo(length,std::vector<bool>(length));
		for(int i = 0;i < length;i ++) {
			memo[i][i] = 1;
		}
		for(int i = 0;i < length - 1;i++) {
			memo[i][i + 1] = (s[i] == s[i+1]);
			if(memo[i][i + 1]) {
				maxLength = 2;
				start = i;
			}
		}
		for(int localLength = 3;localLength <= length;localLength++) {
			for(int i = 0 ; i < length - localLength + 1;i++) {
				memo[i][i + localLength - 1] = memo[i + 1][i + localLength -2] && (s[i] == s[i + localLength - 1]);
				if(memo[i][i + localLength - 1]) {
					maxLength = localLength;
					start = i;
				}
			}
		}
		return s.substr(start,maxLength);
    }
};

int main() {
	std::string test = "abba";
	Solution* sol = new Solution();
	std::string result = sol->longestPalindrome(test);
	std::cout << result << std::endl;
	return 1;
}
