#include "common.h"

#include <iostream>

void print_vector(const std::vector<int> &values)
{
    for (const auto &value : values)
    {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

//
// Linked List
//
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

//
// Binary Tree
//
TreeNode *create_binary_tree(const std::vector<int> &values)
{
    if (values.empty())
        return nullptr;

    std::queue<TreeNode *> q;
    TreeNode *root = new TreeNode(values[0]);
    q.push(root);
    int i = 1;

    while (!q.empty())
    {
        TreeNode *node = q.front();
        q.pop();
        if (i < values.size() && values[i] != NULL_VALUE)
        {
            node->left = new TreeNode(values[i]);
            q.push(node->left);
        }
        i++;
        if (i < values.size() && values[i] != NULL_VALUE)
        {
            node->right = new TreeNode(values[i]);
            q.push(node->right);
        }
        i++;
    }

    return root;
}
