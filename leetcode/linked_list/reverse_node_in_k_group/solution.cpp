#include <stack>
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
		std::stack<ListNode*> nodes;
		ListNode *tail,*prev,*cur,*temp = head;
		int i;
		for (i = 0; i < k && temp!= nullptr; ++i) 
		{
			nodes.push(temp);
			temp = temp->next;
		}
		if(i == k) // remain list has at least k nodes
		{
			prev = tail = nodes.top();
			temp = tail->next;
			nodes.pop();
			while(!nodes.empty())
			{
				cur = nodes.top();
				nodes.pop();
				prev->next = cur;
				prev =cur;
			}
			prev->next = reverseKGroup(temp,k);
			return tail;
		}
		else // remain list doesn't have k nodes
		{
			return head;
		}
    }
};
