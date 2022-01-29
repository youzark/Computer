#include <iostream>
#include <string>
#include <string_view>

class Solution {
public:
    bool isMatch(std::string s, std::string p) {
		return solver(std::string_view(s.c_str(),s.length()),std::string_view(p.c_str(),p.length()));
    }
	bool solver(std::string_view s, std::string_view p) {
		if(p.empty()) {
			return s.empty();
		} else if (s.empty()) {
			if(p.length() % 2 != 0) {
				return 0;
			} else {
				return (p[1] == '*') && solver(s,p.substr(2,p.length()-2));
			}
		}
		if(p[0] != '.' && p[1] != '*') {
			return p[0] == s[0] && solver(s.substr(1,s.length() - 1),p.substr(1,p.length() - 1));
		} else if(p[1] == '*') {
			int skipLength = 0;
			while(skipLength <= s.length()) {
				if(skipLength != 0 && s[skipLength - 1] != p[0] && p[0] != '.') {
					break;
				}
				if(solver(s.substr(skipLength,s.length() - skipLength),p.substr(2,p.length() - 2))) {
					return 1;
				}
				skipLength ++;
			}
			return 0;
		} else {
			return solver(s.substr(1,s.length() - 1),p.substr(1,p.length() - 1));
		}
	}
};

int main() {
	Solution* sol = new Solution();
	std::cout << sol->isMatch("aa","a*") << std::endl;
	return 1;
}
