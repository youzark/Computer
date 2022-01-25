#include <iostream>
#include <string>
#include <map>
#include <tuple>
class Solution {
public:
	std::map<std::tuple<int,int>,bool> memo;
	std::string longestPalindrome(std::string s) {
		int start = 0;
		int length = s.length();
		int end = 0;
		int maxlength=1;
		for(int i = 0;i < length;i ++){
			memo.insert(std::pair<std::tuple<int,int>,bool>(std::tuple<int,int>(i,i),1));
			memo.insert(std::pair<std::tuple<int,int>,bool>(std::tuple<int,int>(i,i+1),(s[i] == s[i+1])));
		}

		for(int i = length - 1;i >= 0;i--) {
			for(int j = i + maxlength - 1; j < length; j++) {
				if(isPalindorme(i,j,s)) {
					start = i;
					end = j;
					maxlength = j - i + 1;
				}
			}
		}
		return s.substr(start,end-start + 1);
    }
	bool isPalindorme(int i,int j,std::string& s)
	{
		auto item = memo.find(std::tuple<int,int>(i,j));
		if(item == memo.end()) {
			bool isPal = isPalindorme(i + 1,j - 1,s) && (s[i] == s[j]);
			memo.insert(std::pair<std::tuple<int,int>,bool>(std::tuple<int,int>(i,j),isPal));
			return isPal;
		} else {
			return item->second;
		}
	}
};

int main() {
	std::string test = "whyadafadshfaosdihfaod";
	Solution* sol = new Solution();
	std::string result = sol->longestPalindrome(test);
	std::cout << result << std::endl;
	return 1;
}
