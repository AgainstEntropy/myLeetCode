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

ListNode *create_cycle_linked_list(const std::vector<int> &values, int pos)
{

    ListNode *head = create_linked_list(values);
    if (pos == -1)
        return head;

    ListNode *curr = head;
    ListNode *cycle_node;
    for (int i = 0; i < pos; ++i)
    {
        curr = curr->next;
    }
    cycle_node = curr;

    while (curr->next)
    {
        curr = curr->next;
    }
    curr->next = cycle_node;

    return head;
}

void print_vector(const std::vector<int> &values)
{
    for (const auto &value : values)
    {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}
