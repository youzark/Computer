#include <iostream>
// note : to get O(nlogn) and O(1) sort on linked list
// usually we use merge sort instead of quick sort
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* sortList(ListNode* head) 
	{
    }
	ListNode* merge_two_part(ListNode* head)
	{
	}
};
