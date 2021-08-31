struct ListNode 
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
	// some improvement to avoid annoying boundary checking
    ListNode* swapNodes(ListNode* head, int k) 
	{

		ListNode *vart = new ListNode(0);
		ListNode *cur = head,*prev1 = vart,*prev2 = vart;
		ListNode *temp,*node1,*node2;
		vart->next = head;
		head = vart;

		// find pos for prev1 and prev2
		for (int i = 0; i < k-1; ++i) 
		{
			cur = cur->next;
			prev1 = prev1->next;
		}
		// prve1 stops at the k-1(th) node , cur point to the kth node
		// treat vart(prev2) as head,then cur points to k+1(th) node
		while(cur->next) // it's guaranteed cur has at least one next(can be null)
		{
			cur = cur->next;
			prev2 = prev2->next;
		}

		if(prev2 == prev1)
		{
			return head->next;
		}
		else if(prev1->next == prev2)
		{
			node1 = prev2;
			node2 = node1->next;
			temp = node2->next;
			prev1->next = node2;
			node2->next = node1;
			node1->next = temp;
		}
		else if(prev2->next == prev1)
		{
			node1 = prev1;
			node2 = node1->next;
			temp = node2->next;
			prev2->next = node2;
			node2->next = node1;
			node1->next = temp;
		}
		else
		{
			node1 = prev1->next;
			node2 = prev2->next;
			temp = node2->next;
			prev1->next = node2;
			node2->next = node1->next;
			prev2->next = node1;
			node1->next = temp;
		}
		return head->next;
    }
};
