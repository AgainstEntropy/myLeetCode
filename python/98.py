# 验证二叉搜索树
# Validate Binary Search Tree

from common import Optional, TreeNode, Tuple, create_binary_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.validMinMax(root)[0]

    def validMinMax(self, node: Optional[TreeNode]) -> Tuple[bool, int, int]:
        if node.left is None and node.right is None:
            return True, node.val, node.val

        elif node.left is None and node.right is not None:
            rValid, rMin, rMax = self.validMinMax(node.right)
            valid = rValid and node.val < rMin
            return valid, min(node.val, rMin), max(node.val, rMax)

        elif node.left is not None and node.right is None:
            lValid, lMin, lMax = self.validMinMax(node.left)
            valid = lValid and node.val > lMax
            return valid, min(node.val, lMin), max(node.val, lMax)

        else:
            lValid, lMin, lMax = self.validMinMax(node.left)
            rValid, rMin, rMax = self.validMinMax(node.right)
            valid = lValid and rValid and lMax < node.val < rMin
            return valid, min(node.val, lMin, rMin), max(node.val, lMax, rMax)


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3],),
        ([5, 1, 4, None, None, 3, 6],),
        ([5, 1, 6, None, None, 4, 7],),
    ]
    sol = Solution()
    for case in test_cases:
        print(sol.isValidBST(create_binary_tree(case[0])))
