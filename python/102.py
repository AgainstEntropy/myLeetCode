# 二叉树的层序遍历
# Binary Tree Level Order Traversal

from common import List, Optional, TreeNode, create_binary_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        if not root:
            return result

        from collections import deque

        queue = deque([(root, 0)])

        while len(queue):
            node, level = queue.popleft()
            if node is None:
                continue
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return result


if __name__ == "__main__":
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1],
        [],
    ]
    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case)
        print(sol.levelOrder(root))
