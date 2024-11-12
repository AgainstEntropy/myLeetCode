# 二叉树的最近公共祖先
# Lowest Common Ancestor of a Binary Tree

from common import Optional, TreeNode, create_binary_tree, find_node


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        ancestors: dict[TreeNode, tuple[TreeNode]] = {}
        children = {p, q}
        stack = []

        def visit(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            stack.append(node)
            if node in children:
                ancestors[node] = tuple(stack)
                children.remove(node)
                return True
            if visit(node.left):
                return True
            if visit(node.right):
                return True
            stack.pop()
            return False

        visit(root)

        def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if root is None:
                return None
            if root.val == val:
                return root
            return find_node(root.left, val) or find_node(root.right, val)

        node1, ancestors = list(ancestors.items())[0]
        node2 = children.pop()

        for i in range(len(ancestors) - 1, -1, -1):
            if i < len(ancestors) - 1:
                if ancestors[i + 1] == ancestors[i].left:
                    if find_node(ancestors[i].right, node2.val):
                        return ancestors[i]
                else:
                    if find_node(ancestors[i].left, node2.val):
                        return ancestors[i]
            else:
                if find_node(ancestors[i], node2.val):
                    return ancestors[i]


if __name__ == "__main__":
    test_cases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4),
        ([1, 2], 1, 2),
    ]

    sol = Solution()
    for root, p, q in test_cases:
        root = create_binary_tree(root)
        p_node = find_node(root, p)
        q_node = find_node(root, q)
        print(sol.lowestCommonAncestor(root, p_node, q_node).val)
