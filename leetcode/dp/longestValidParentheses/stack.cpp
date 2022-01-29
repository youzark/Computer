#include <iostream>
#include <stack>
#include <string>

class Solution {
public:
    int longestValidParentheses(std::string s) {
		int length = s.length();
		int maxLength = 0;
		std::stack<int> *track = new std::stack<int>();
		track->push(-1);
		for(int i = 0; i < length; i++) {
			if(s[i] == ')') {
				track->pop();
				if(track->empty()) {
					track->push(i);
				} else {
					maxLength = (i - track->top()) > maxLength ? i - track->top() : maxLength;
				}
			} else {
				track->push(i);
			}
		}
		return maxLength;
    }
};

int main() {
	Solution * sol = new Solution();
	std::cout << sol->longestValidParentheses(")(())");
	return 1;
}

