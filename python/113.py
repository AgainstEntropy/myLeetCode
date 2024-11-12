# 路径总和 II
# Path Sum II

from common import List, Optional, TreeNode, create_binary_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []

        node_stack = []
        sum_stack = [0]

        def visit(node: Optional[TreeNode]):
            if node is None:
                return

            node_stack.append(node.val)
            sum_stack.append(sum_stack[-1] + node.val)
            if node.left is None and node.right is None and sum_stack[-1] == targetSum:
                results.append(node_stack.copy())

            visit(node.left)
            visit(node.right)

            node_stack.pop()
            sum_stack.pop()

        visit(root)

        return results


if __name__ == "__main__":
    test_cases = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22),
        ([1, 2, 3], 5),
        ([1, 2], 0),
    ]

    sol = Solution()
    for arr, target in test_cases:
        root = create_binary_tree(arr)
        print(sol.pathSum(root, target))
