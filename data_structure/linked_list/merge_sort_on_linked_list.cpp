#include <iostream>
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
		if(!head || !head->next)
		{
			ListNode *mid = FindMid(head);
			ListNode *right_part_head = sortList(head),*left_part_head;
			ListNode *left_part_end;
		}
		return head;
    }

	// when called head has at least 2 nodes
	ListNode *FindMid(ListNode *head)
	{
		// when slow == the 2^i node fast -> the 2^i ~ 2^(i+1)-1
		ListNode *mid;
		ListNode *fast = head,*slow = head;
		int step = 1,count;
		while(!fast)
		{
			count = 0;
			while(count != step && !fast)
			{
				fast = fast->next;
				count ++;
			}
			if(!fast)
			{
				mid = slow;
				slow = fast;
				step *=2;
			}
			else
			{
				int remain = count / 2;
				while(remain != 0)
				{
					mid = mid->next;
					remain ++;
				}
			}
		}
		return head;
	}

	ListNode* partition(ListNode* list,ListNode* right_part_head,ListNode* left_part_end) // right and left are used to pass value back
	{

	}
};
