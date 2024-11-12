# 路径总和
# Path Sum

from common import Optional, TreeNode, create_binary_tree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [0]

        def visit(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False

            stack.append(stack[-1] + node.val)
            if node.left is None and node.right is None and stack[-1] == targetSum:
                return True

            if visit(node.left):
                return True
            if visit(node.right):
                return True
            stack.pop()
            return False

        return visit(root)


if __name__ == "__main__":
    test_cases = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22),
        ([1, 2, 3], 5),
        ([1, 2], 1)
    ]

    sol = Solution()
    for arr, target in test_cases:
        root = create_binary_tree(arr)
        print(sol.hasPathSum(root, target))
