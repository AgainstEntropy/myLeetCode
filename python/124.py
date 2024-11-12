# 二叉树中的最大路径和
# Binary Tree Maximum Path Sum

from common import Optional, TreeNode, Tuple, create_binary_tree


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.maxOneWaySum(root)[0]

    def maxOneWaySum(self, node: Optional[TreeNode]) -> Tuple[int, int | float]:
        """
        Returns:
            Tuple[int]: (int1, int2)
            int1: max of all possible path with in the sub-tree of which node is the root
            int2: max of passing either (node, node.left) or (node, node.right)
        """

        if node is None:
            return -float("inf"), -float("inf")

        if node.left is None and node.right is None:
            return node.val, node.val

        leftMax, leftOneWayMax = self.maxOneWaySum(node.left)
        rightMax, rightOneWayMax = self.maxOneWaySum(node.right)

        nodeOneWayMax = max(
            node.val, leftOneWayMax + node.val, rightOneWayMax + node.val
        )
        nodeIncludedMax = leftOneWayMax + rightOneWayMax + node.val
        nodeMax = max(leftMax, rightMax, nodeIncludedMax, nodeOneWayMax)

        return nodeMax, nodeOneWayMax


if __name__ == "__main__":
    test_cases = [
        [-1, 5, None, 4, None, None, 2, -4],
        [2, -1],
        [-2, -1],
        [1, 2, 3],
        [-10, 9, 20, None, None, 15, 7],
        [20, 9, -10, None, None, 15, 7],
        [-3],
    ]

    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case)
        print(sol.maxPathSum(root))
