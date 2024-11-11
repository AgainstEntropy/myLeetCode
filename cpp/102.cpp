// 二叉树的层序遍历
// Binary Tree Level Order Traversal

#include "common.h"

class Solution
{
public:
    std::vector<std::vector<int>> levelOrder(TreeNode *root)
    {
        std::vector<std::vector<int>> result = {};
        if (root == nullptr)
        {
            return result;
        }

        std::deque<std::pair<TreeNode *, int>> queue;
        queue.push_back({root, 0});

        while (!queue.empty())
        {
            auto [node, level] = queue.front();
            queue.pop_front();
            if (node == nullptr)
            {
                continue;
            }
            if (level >= result.size())
            {
                result.resize(level + 1);
            }
            result[level].push_back(node->val);
            queue.push_back({node->left, level + 1});
            queue.push_back({node->right, level + 1});
        }

        return result;
    }
};

int main()
{
    std::vector<std::vector<int>> test_cases = {
        {3, 9, 20, NULL_VALUE, NULL_VALUE, 15, 7},
        {1},
        {},
    };

    Solution sol;
    for (const auto &test_case : test_cases)
    {
        auto root = create_binary_tree(test_case);
        auto result = sol.levelOrder(root);
        for (const auto &level : result)
        {
            print_vector(level);
        }
    }
}
