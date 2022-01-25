#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
	// non-recursive dp (bottom up)
    bool isMatch(std::string s, std::string p) {
		int strLength = s.length() , patternLength = p.length();
		// if s[0:i] mathches p[0:j]
		std::vector<std::vector<bool>> memo(patternLength,std::vector<bool>(strLength));
    }
};

int main() {
	Solution* sol = new Solution();
	std::cout << sol->isMatch("aa","a*") << std::endl;
	return 1;
}
