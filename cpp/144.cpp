// 二叉树的前序遍历
// Binary Tree Preorder Traversal

#include "common.h"

class Solution
{
public:
    std::vector<int> preorderTraversal(TreeNode *root)
    {
        std::vector<int> result;
        visit(root, result);
        return result;
    }

    void visit(TreeNode *node, std::vector<int> &result)
    {
        if (node == nullptr)
            return;
        result.push_back(node->val);
        visit(node->left, result);
        visit(node->right, result);
    }
};

int main()
{
    std::vector<std::vector<int>> test_cases = {
        {1, NULL_VALUE, 2, 3},
        {1, 2, 3, 4, 5, NULL_VALUE, 8, NULL_VALUE, NULL_VALUE, 6, 7, 9},
    };

    Solution sol;
    for (const auto &test_case : test_cases)
    {
        TreeNode *root = create_binary_tree(test_case);
        std::vector<int> result = sol.preorderTraversal(root);
        print_vector(result);
    }
}
