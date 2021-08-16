struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) 
	{
		ListNode *front,*head,*temp,*trav1,*next1,*trav2,*next2;
		int at;
		if(l1 == nullptr)
		{
			return l2;
		}
		if(l2 == nullptr)
		{
			return l1;
		}
		if(l1->val < l2->val)
		{
			front = head = l1;
			ListNode *vhead = new ListNode(0,l2);
			trav1 = l1;
			trav2 = vhead;
			next1 = trav1->next;
			next2 = trav2->next;
			at = 1;
		}
		else
		{
			front = head = l2;
			ListNode *vhead = new ListNode(0,l1);
			trav1 = vhead;
			trav2 = l2;
			next1 = trav1->next;
			next2 = trav2->next;
			at = 2;
		}

		while(next1 != nullptr && next2 != nullptr)
		{
			if(next1->val < next2->val)
			{
				trav1 = next1;
				next1 = next1->next;
				if(at == 2)
				{
					front->next = trav1;
					front = front->next;
					at = 1;
				}
			}
			else
			{
				trav2 = next2;
				next2 = next2->next;
				if(at == 1)
				{
					front->next = trav2;
					front = front->next;
					at = 1;
				}
			}
		}
		if(next1 == nullptr)
		{
			trav1->next = trav2;
		}
		else
		{
			trav2->next = trav1;
		}
		return head;
    }
};
