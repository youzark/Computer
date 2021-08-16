struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
		// to delete the nth element backward ,we get keep track of the n+1th node backword
		ListNode *trav = head,*np1th = head; // np1th->next = nth or nullptr
		/* ListNode *nth = head->next; //when head point to null ,nth point to the nth backward. */
		for (int i = 0; i < n; ++i) // at least n nodes ,can step at least n steps
		{
			trav = trav->next;
		}
		if(trav == nullptr)
		{
			ListNode *ret = head->next;
			delete head;
			return ret;
		}
		while(trav->next != nullptr)
		{
			trav = trav->next;
			np1th = np1th->next;
		}
		ListNode *nth = np1th->next;
		np1th->next = nth->next;
		delete nth;
		return head;
    }
};
