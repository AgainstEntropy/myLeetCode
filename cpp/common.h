#pragma once

#include <vector>
#include <queue>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* create_linked_list(const std::vector<int>& values);

void print_linked_list(ListNode* head);

ListNode* create_cycle_linked_list(const std::vector<int>& values, int pos);

void print_vector(const std::vector<int> &values);
