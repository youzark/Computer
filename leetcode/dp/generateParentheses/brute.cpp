#include <iostream>
#include <vector>
#include <string>
#include <stack>
class Solution {
public:
	std::vector<std::string> *parenthesis;
    std::vector<std::string> generateParenthesis(int n) {
		parenthesis = new std::vector<std::string>(0);
		std::string init("");
		backtracking(init,n,n);
		return *parenthesis;
    }
	void backtracking(std::string &str,int leftP,int rightP) {
		if(leftP == 0 && rightP == 0) {
			parenthesis->push_back(str);
			return;
		}
		if(leftP != 0) {
			str.push_back('(');
			backtracking(str ,leftP - 1,rightP);
			str.pop_back();
		}
		if(rightP != 0 && rightP > leftP) {
			str.push_back(')');
			backtracking(str,leftP,rightP - 1);
			str.pop_back();
		}
		return;
	}
};

int main() {
	Solution *sol = new Solution();
	for(int i = 1;i < 5; i++) {
		std::cout << "******************************* number : " << i << std::endl;
		auto pars = sol->generateParenthesis(i);
		for(auto str : pars) {
			std::cout << str << std::endl;
		}
	}
	return 1;
}
