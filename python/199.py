# 二叉树的右视图
# Binary Tree Right Side View

from common import List, Optional, TreeNode, Tuple, create_binary_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels: List[List] = []
        stack: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]

        while len(stack) > 0:
            nodeL = stack.pop(0)
            if nodeL is None:
                continue

            node, level = nodeL
            if node is None:
                continue

            if level >= len(levels):
                levels.append([])

            levels[level].append(node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

        return [level[-1] for level in levels]


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, None, 5, None, 4],
        [1, None, 3],
        [],
    ]

    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case)
        print(sol.rightSideView(root))
