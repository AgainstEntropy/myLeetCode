# 平衡二叉树
# Balanced Binary Tree

from common import Optional, TreeNode, create_binary_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.validateHeight(root)[0]

    def validateHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return True, 0

        lValid, lHeight = self.validateHeight(node.left)
        rValid, rHeight = self.validateHeight(node.right)

        if lValid and rValid and abs(lHeight - rHeight) <= 1:
            return True, max(lHeight, rHeight) + 1

        return False, -1


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7],),
        ([1, 2, 2, 3, 3, None, None, 4, 4],),
        ([],),
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.isBalanced(create_binary_tree(case[0])))
