# 二叉树的直径
# Diameter of Binary Tree

from common import Optional, TreeNode, Tuple, create_binary_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.calculateMax(root)[0]

    def calculateMax(self, node: Optional[TreeNode]) -> Tuple[int, int]:

        if node is None:
            return 0, -1

        maxLeft, maxLeftOneWay = self.calculateMax(node.left)
        maxRight, maxRightOneWay = self.calculateMax(node.right)

        maxIncludNode = max(maxLeft, maxRight, maxLeftOneWay + maxRightOneWay + 2)
        maxOneWay = max(maxLeftOneWay, maxRightOneWay) + 1

        return maxIncludNode, maxOneWay


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
    ]
    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case)
        res = sol.diameterOfBinaryTree(root)
        print(res)
