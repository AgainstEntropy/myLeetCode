# 二叉树最大宽度
# Maximum Width of Binary Tree

from common import List, Optional, TreeNode, Tuple, create_binary_tree


class Solution:
    def widthOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        """
        Fill all vacant places with a TreeNode(TAG_VAL)
        Time limit exceeded
        """
        TAG_VAL = float("inf")

        levels: List[List[Optional[TreeNode]]] = []
        level_all_taged = []
        stack: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]

        while len(stack) > 0:
            node, level = stack.pop(0)

            if level >= len(levels):
                if level_all_taged and level_all_taged[-1]:
                    break
                levels.append([])
                level_all_taged.append(True)

            levels[level].append(node)
            if node is None:
                continue

            if node.val != TAG_VAL:
                level_all_taged[level] = False

            if node.left is None:
                node.left = TreeNode(TAG_VAL)
            if node.right is None:
                node.right = TreeNode(TAG_VAL)

            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

        levels = levels[:-1]

        for i, level in enumerate(levels):
            start = 0
            while level[start] is None or level[start].val == TAG_VAL:
                start += 1

            end = len(level)
            while level[end - 1] is None or level[end - 1].val == TAG_VAL:
                end -= 1

            levels[i] = level[start:end]

        return max(list(map(len, levels)))

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        levels: List[List[Tuple[TreeNode, int]]] = []
        stack: List[Tuple[TreeNode, int, int]] = [(root, 0, 1)]

        while len(stack) > 0:
            node, level, pos = stack.pop(0)

            if level >= len(levels):
                levels.append([])

            levels[level].append(pos)

            if node.left:
                stack.append((node.left, level + 1, pos * 2 - 1))
            if node.right:
                stack.append((node.right, level + 1, pos * 2))

        levels_width = [level[-1] - level[0] + 1 for level in levels if len(level) >= 2]
        maxWidth = max(levels_width) if levels_width else 1

        return maxWidth


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 2, 5, None, None, 9, 6, None, 7], 7),
        ([-64,12,18,-4,-53,None,76,None,-51,None,None,-93,3,None,-31,47,None,3,53,-81,33,4,None,-51,-44,-60,11,None,None,None,None,78,None,-35,-64,26,-81,-31,27,60,74,None,None,8,-38,47,12,-24,None,-59,-49,-11,-51,67,None,None,None,None,None,None,None,-67,None,-37,-19,10,-55,72,None,None,None,-70,17,-4,None,None,None,None,None,None,None,3,80,44,-88,-91,None,48,-90,-30,None,None,90,-34,37,None,None,73,-38,-31,-85,-31,-96,None,None,-18,67,34,72,None,-17,-77,None,56,-65,-88,-53,None,None,None,-33,86,None,81,-42,None,None,98,-40,70,-26,24,None,None,None,None,92,72,-27,None,None,None,None,None,None,-67,None,None,None,None,None,None,None,-54,-66,-36,None,-72,None,None,43,None,None,None,-92,-1,-98,None,None,None,None,None,None,None,39,-84,None,None,None,None,None,None,None,None,None,None,None,None,None,-93,None,None,None,98], 169),
        ([1, None, 2], 1),
        ([1, 3, 2, 5, 3, None, 9], 4),
        ([1, 3, 2, 5, None, None, None], 2),
    ]
    for arr, ans in test_cases:
        root = create_binary_tree(arr)
        print(Solution().widthOfBinaryTree(root))
