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
		ListNode *front,*head,*edge1,*edge2;

		edge1 = l1;
		edge2 = l2;
		if(edge1 == nullptr)
		{
			return edge2;
		}
		if(edge2 == nullptr)
		{
			return edge1;
		}
		//guarantee l1 and l2 are not empty

		// front is the last node we add to the ans.linked_list
		// edge is the two node(or null) waiting to be appended to ans

		// init front and edge
		front = edge1->val < edge2->val ? edge1 : edge2;
		head = front;
		// caution here :
		// in one scope
		// if you edit one pointer(edge1 here)
		// don't visit it's member again unless you can verifiy it is not null
		// edit edge1 and edge2 are logically parallel ,should be executed in parallel 
		// if sequence does affect
		bool comp = edge1->val < edge2->val;
		edge1 = comp  ? edge1->next : edge1;
		edge2 = comp  ? edge2 : edge2->next;

		while(edge1 != nullptr && edge2 != nullptr)
		{
			if(edge1->val < edge2->val)
			{
				front->next = edge1;
				edge1 = edge1->next;
				front = front->next;
			}
			else
			{
				front->next = edge2;
				edge2 = edge2->next;
				front = front->next;
			}
		}
		front->next = (edge1 == nullptr) ? edge2 : edge1;
		return head;
    }
};
