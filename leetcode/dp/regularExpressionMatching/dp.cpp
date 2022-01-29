#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
	// non-recursive dp (bottom up)
    bool isMatch(std::string s, std::string p) {
		int strLength = s.length() , patternLength = p.length();

		// memo[i][j] : if s[0:i - 1] matched p[0:j - 1]
		// memo[0][:] and memo[:][0] are dummy row and column
		// if p[j - 1] == '*'  : memo[i][j] depend on memo[i][j-2] or memo[i-1][j]
		// if p[j - 1] != '*'  : memo[i][j] depend on memo[i-1][j-1]
		// wanted value : memo[strLength][patternLength]
		std::vector<std::vector<bool>> memo(strLength + 1,std::vector<bool>(patternLength + 1,false));

		memo[0][0] = true;
		for(int i = 0;i <= strLength; i ++) {
			for(int j = 1; j <= patternLength; j ++) {
				if(p[j - 1] == '*') {
					memo[i][j] = memo[i][j - 2] || ((i != 0) && memo[i - 1][j] && ((s[i - 1] == p[j - 2]) || p[j - 2] == '.'));
				} else {
					memo[i][j] = (i != 0) && (memo[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == '.'));
				}
			}
		}
		return memo[strLength][patternLength];
    }
};
int main() {
	Solution* sol = new Solution();
	std::cout << sol->isMatch("aab","b.*") << std::endl;
	return 1;
}
