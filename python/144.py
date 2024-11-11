# 二叉树的前序遍历
# Binary Tree Preorder Traversal

from common import List, Optional, TreeNode, create_binary_tree


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def visit(node: Optional[TreeNode], res: List[int]):
            if node is None:
                return
            res.append(node.val)
            visit(node.left, res)
            visit(node.right, res)

        visit(root, res)

        return res


if __name__ == "__main__":
    test_cases = [
        ([1, None, 2, 3],),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],),
    ]
    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case[0])
        print(sol.preorder_traversal(root))
