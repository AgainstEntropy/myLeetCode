# 二叉树的最大深度
# Maximum Depth of Binary Tree

from common import Optional, TreeNode, create_binary_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ]

    sol = Solution()
    for arr, ans in test_cases:
        root = create_binary_tree(arr)
        print(sol.maxDepth(root))
