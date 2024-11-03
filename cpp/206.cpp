// Reverse Linked List
// 反转链表

#include "common.h"

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *prev = nullptr;
        ListNode *curr = head;
        ListNode *next;
        while (curr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};

int main()
{
    std::vector<int> values = {1, 2, 3, 4, 5};
    ListNode *head = create_linked_list(values);
    print_linked_list(head);

    Solution sol;
    ListNode *res = sol.reverseList(head);
    print_linked_list(res);
}