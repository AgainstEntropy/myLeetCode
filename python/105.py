# 从前序与中序遍历序列构造二叉树
# Construct Binary Tree from Preorder and Inorder Traversal

from common import Optional, TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        k = 0
        while inorder[k] != root.val:
            k += 1

        left_inorder = inorder[:k]
        right_inorder = inorder[k + 1 :]

        left_preorder = preorder[1 : 1 + k]
        right_preorder = preorder[1 + k :]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([-1], [-1]),
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.buildTree(*case))
