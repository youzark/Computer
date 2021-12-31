#include <initializer_list>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
	ListNode(std::initializer_list<int> init)
	{
		for(auto elem : init)
		{
		}

	}
	void emplace_front(int elem)
	{

	}
};
