 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
	{
		ListNode* solution = new ListNode();
		ListNode* start = solution;
		int in = 0;
		while(l1 != nullptr && l2 != nullptr)
		{
			solution->next = new ListNode();
			solution = solution->next;
			solution->val = (l1->val + l2->val + in)%10;
			in = (l1->val + l2->val + in) / 10;
			l1 = l1->next;
			l2 = l2->next;
		}
		if(l1 == nullptr)
		{
			while(l2 != nullptr)
			{
				solution->next = new ListNode();
				solution = solution->next;
				solution->val = (l2->val + in)%10;
				in = (l2->val + in) / 10;
				l2 = l2->next;
			}
		}
		else
		{
			while(l1 != nullptr)
			{
				solution->next = new ListNode();
				solution = solution->next;
				solution->val = (l1->val + in)%10;
				in = (l1->val + in) / 10;
				l1 = l1->next;
			}
		}
		if(in == 1)
		{
			solution->next = new ListNode(1);
		}
		return start->next;
    }
};
