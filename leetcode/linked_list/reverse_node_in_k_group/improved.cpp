#include <tuple>
#include <utility>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// this solution is deprecated
class Solution 
{
public:
    ListNode* reverseKGroup(ListNode* head, int k) 
	{
		ListNode *nh,*next,temp;
		if(k == 1)
		{
			return head;
		}
		auto rt = sim_reverse(head,k);
		nh = rt.first;
		next = rt.second;
		if(!nh) 
		{
			/* sim_reverse(,k); // reverse it back */
			return head;
		}
		head->next = sim_reverse(next,k).first;
		return nh;
    }
	std::pair<ListNode *,ListNode *> sim_reverse(ListNode* head,int k)
	{
		ListNode *tail,*prev,*cur = nullptr,*temp;
		int i;
		if(!head)
		{
			return std::pair<ListNode *,ListNode *>(head,nullptr);
		}
		prev = head;
		for (i = 0; i < k && prev->next; ++i) 
		{
			cur = prev->next;
			tail = cur->next;
			temp = prev;
			prev = cur;
			cur->next = temp;
		}
		return i == k ? std::pair<ListNode *,ListNode *>(cur,tail) : std::pair<ListNode *,ListNode *>(nullptr,nullptr);
	}
};

