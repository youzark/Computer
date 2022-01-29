#include <iostream>
#include <string>
#include <string_view>
#include <algorithm>

// I don't know if this is a valid algorithm , but clearly I misunderstood the problem,
// I didn't get the meaning of * in the problem , so this method is depricated.
class Solution {
public:
    bool isMatch(std::string s, std::string p) {
		return solver(std::string_view(s.c_str(),s.length()),std::string_view(p.c_str(),p.length()));
    }
	bool solver(std::string_view s, std::string_view p) {
		if(s.empty() || p.empty()) {
			return s.empty() && p.empty();
		}
		if(p[0] != '.' && p[0] != '*') {
			return p[0] == s[0] && solver(s.substr(1,s.length() - 1),p.substr(1,p.length() - 1));
		} else if(p[0] == '.') {
			return solver(s.substr(1,s.length() - 1),p.substr(1,p.length() - 1));
		} else {
			int skipLength = 0;
			while(skipLength <= s.length()) {
				if(solver(s.substr(skipLength,s.length() - skipLength),p.substr(1,p.length() - 1))) {
					return 1;
				}
				skipLength ++;
			}
			return 0;
		}
	}
};

int main() {
	Solution* sol = new Solution();
	std::cout << sol->isMatch("asdfadf","*.d.") << std::endl;
	return 1;
}
