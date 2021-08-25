struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
		// if only one or zero node,just return
		if(!head || !head->next)
		{
			return head;
		}
		ListNode *temp = head->next;
		head->next = swapPairs(temp->next);
		temp->next = head;
		return temp;
    }
};
