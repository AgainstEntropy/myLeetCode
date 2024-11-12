# 翻转二叉树
# Invert Binary Tree

from common import Optional, TreeNode, create_binary_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


if __name__ == "__main__":
    test_cases = [
        [4, 2, 7, 1, 3, 6, 9],
        [2, 1, 3],
        [],
    ]

    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case)
        print(sol.invertTree(root))
