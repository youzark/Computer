struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution 
{
public:
    ListNode* reverseKGroup(ListNode* head, int k) 
	{
		ListNode *prev,*cur,*temp;
		int i = 0;
		if(!head || !head->next) // at least one node
		{
			return head;
		}
		prev = head;
		cur = prev->next;
		for (i = 0; i < k - 1 && cur; ++i) 
		{
			temp = cur->next;
			cur->next = prev;
			prev = cur;
			cur = temp;
		}
		if(i == k - 1)
		{
			head->next = reverseKGroup(cur,k);
			return prev;
		}
		else // reverse remaining, cur == nullptr
		{
			ListNode *tail = prev;
			cur = prev->next;
			while(!cur)
			{
				temp = cur->next;
				cur->next = prev;
				prev = cur;
				cur = temp->next;
			}
			tail->next = nullptr;
			return cur;
		}
    }
};

