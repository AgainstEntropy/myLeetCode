#pragma once

#include <iostream>
#include <vector>
#include <queue>

void print_vector(const std::vector<int> &values);

// Definition for singly-linked list.
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

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* create_binary_tree(const std::vector<int>& values);

#define NULL_VALUE -1
