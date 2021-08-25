#include <queue>
#include <vector>
#include <limits.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) 
	{
		ListNode dummyHead(0);
		ListNode *front = &dummyHead;
		
		// clear out null situations 
		if (lists.size() == 0) 
		{
			return nullptr;
		}

		// comparator function
		auto comp = [](ListNode *l,ListNode *r)
		{
			return l->val > r->val;
		};
		
		std::priority_queue<ListNode *,std::vector<ListNode*>,decltype(comp)> pq(comp);

		for(ListNode *node:lists)
		{
			if(node)
			{
				pq.push(node);
			}
		}

		while(!pq.empty())
		{
			auto target = pq.top();
			pq.pop();
			
			front->next = target;
			front = front->next;

			if(target->next)
			{
				pq.push(target->next);
			}
		}

		front->next = nullptr;
		return dummyHead.next;
    }
};

