struct ListNode 
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// first naive solution
// what a bad taste!!!
// don't want to see such a unelegant method
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) 
	{
		// first find k-1,k from start

		if(!head->next)
		{
			return head;
		}
		if(k == 1)
		{
			ListNode *end = head;
			while(end->next->next)
			{
				end = end->next;
			}
			ListNode *temp = end->next;
			if(head->next != temp)
			{
				temp->next = head->next;
			}
			else
			{
				temp->next = head;
			}
			end->next = head;
			head->next = nullptr;
			return temp;
		}
		ListNode *km1,*kp1;
		ListNode *front=head;
		for (int i = 0; i < k-2; ++i) 
		{
			front = front->next;
		}


		km1 = front;
		// it's guaranteed that km1->next is not empty
		// here we assume km1 != k , which will be violated if only one node exists
		
		front = km1->next->next;
		// distance from first to front is k+1
		ListNode *first = head;

		// we get only k node
		if(!front)
		{
			front = km1->next;  // new head
			if(km1 == head)
			{
				front->next = head;
			}
			else
			{
				front->next = head->next;
			}
			km1->next = head;
			head->next = nullptr;
			return front;
		}
		// then find k+1,k from end and figure out relation with kth from start
		int step = 0;
		ListNode *fk;
		ListNode *bk;
		ListNode *temp;
		ListNode *fmk;
		ListNode *bpk;
		while(front->next)  // if(!front) make sure front->next valid
		{
			first = first->next;
			front = front->next;
			step++;
		}
		kp1 = first;
		if(step + 2 == k) // kth from start == from end
		{
			return head;
		}
		else if(step + 2 > k)
		{
			fk = km1->next;
			bk = kp1->next;
			temp = bk->next;
			fmk = km1;
			bpk = kp1;
		}
		else
		{
			fk = kp1->next;
			bk = km1->next;
			temp = bk->next;
			fmk = kp1;
			bpk = km1;
		}
		if(step + 3 == k || step + 1 == k)
		{
			fmk->next = bk;
			bk->next = fk;
			fk->next = temp;
			return head;
		}
		fmk->next = bk;
		bk->next = fk->next;
		bpk->next = fk;
		fk->next = temp;
		return head;
    }
};
