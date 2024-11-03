#include "common.h"

#include <iostream>

ListNode *create_linked_list(const std::vector<int> &values)
{
    if (values.empty())
        return nullptr;
    ListNode *head = new ListNode(values[0]);
    ListNode *curr = head;
    for (int i = 1; i < values.size(); ++i)
    {
        curr->next = new ListNode(values[i]);
        curr = curr->next;
    }
    return head;
}

void print_linked_list(ListNode *head)
{
    ListNode *curr = head;
    while (curr)
    {
        std::cout << curr->val << " -> ";
        curr = curr->next;
    }
    std::cout << "null" << std::endl;
}
