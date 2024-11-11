# 二叉树的中序遍历
# Binary Tree Inorder Traversal

from common import List, Optional, TreeNode, create_binary_tree


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def visit(node: Optional[TreeNode], res: List[int]):
            if node is None:
                return
            visit(node.left, res)
            res.append(node.val)
            visit(node.right, res)

        visit(root, res)

        return res


if __name__ == "__main__":
    test_cases = [
        ([1, None, 2, 3],),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],),
        ([],),
        ([1],),
    ]
    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case[0])
        print(sol.inorder_traversal(root))
