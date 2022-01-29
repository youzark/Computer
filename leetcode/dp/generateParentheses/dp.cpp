#include <iostream>
#include <vector>
#include <string>
class Solution {
public:
	// dp(0) = ""
	// dp(1) = "()"
	// dp(2) = ( dp(0) ) dp(1)  +  (dp(1)) dp(0)
	// dp(3) = ( dp(0) ) dp(2)  +  ( dp(1) ) dp(1) +  ( dp(2) ) dp(0)
    std::vector<std::string> generateParenthesis(int n) {
		std::vector<std::vector<std::string>> memo(n+1);
		memo[0].push_back("");
		memo[1].push_back("()");
		for( int i = 2; i < n + 1; i++ ) {
			for ( int j = 0 ; j < i ; j++ ) {
				for ( auto strInternal : memo[j] ) {
					for ( auto strOuternal : memo[ i - j - 1 ] ) {
						memo[i].push_back("("+strInternal+")" + strOuternal);
					}
				}
			}
		}
		return memo[n];
    }
};

int main() {
	Solution * sol = new Solution();
	auto parSet = sol->generateParenthesis(4);
	for (auto str : parSet) {
		std::cout << str << std::endl;
	}
	return 1;
}
