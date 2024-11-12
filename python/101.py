# 对称二叉树
# Symmetric Tree

from common import Optional, List, Tuple, TreeNode, create_binary_tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def check(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left is None and right is None:
                return True
            elif left is None and right is not None:
                return False
            elif left is not None and right is None:
                return False
            elif left.val != right.val:
                return False

            return check(left.left, right.right) and check(right.left, left.right)

        return check(root.left, root.right)

    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        levels: List[List] = []
        stack: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]

        while len(stack) > 0:
            nodeL = stack.pop(0)
            if nodeL is None:
                continue

            node, level = nodeL
            if level >= len(levels):
                levels.append([])

            levels[level].append(node.val if node else -float("inf"))
            if node is None:
                continue
            else:
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))

        for level_vals in levels:
            n = len(level_vals)
            for i in range(n // 2):
                if level_vals[i] != level_vals[n - 1 - i]:
                    return False

        return True


if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3, 4, 4, 3],
        [1, 2, 2, None, 3, None, 3],
        [1, 2, 2, 3, 4, 4, 3, 5, None, 6, None, 7, 8, None, 9],
        [2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, None, None, 9, 8],
    ]

    sol = Solution()
    for test_case in test_cases:
        root = create_binary_tree(test_case)
        print(sol.isSymmetric(root))
