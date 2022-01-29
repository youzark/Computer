#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    int longestValidParentheses(std::string s) {
		int length = s.length();
		int maxLength = 0;
		std::vector<int> dp(length + 1);
		// add a dumpy header to avoid access dp[-1]
		if(length <= 1) {
			return 0;
		}
		dp[0] = 0;
		dp[1] = 0;
		dp[2] = s[0] == '(' && s[1] == ')' ? 2 : 0;
		for(int i = 2; i < length; i++) {
			if(s[i] == ')') {
				if(s[i-1] == '(') {
					dp[i + 1] = dp[i-1] + 2;
				} else {
					if(dp[i] != 0) {
						dp[i + 1] = (i - 1 -dp[i] != -1) && s[i - 1 -dp[i]] == '(' ? dp[i] + 2 + dp[i - 1 - dp[i]]:0;
					}
				}
			}
		}
		for(int len : dp) {
			maxLength = len > maxLength ? len : maxLength;
		}
		return maxLength;
    }
};

int main() {
	Solution * sol = new Solution();
	std::cout << sol->longestValidParentheses("()(())");
	return 1;
}
