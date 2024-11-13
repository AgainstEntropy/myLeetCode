# 求根节点到叶节点数字之和
# Sum Root to Leaf Numbers

from common import Optional, TreeNode, create_binary_tree


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        stack = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            stack.append(node.val)
            if node.left is None and node.right is None:
                nums.append(self.list2int(stack))

            dfs(node.left)
            dfs(node.right)
            stack.pop()

        dfs(root)

        return sum(nums)

    @staticmethod
    def list2int(num_list: list[int]) -> int:
        return int("".join(list(map(str, num_list))))


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [4, 9, 0, 5, 1],
    ]
    sol = Solution()
    for case in test_cases:
        root = create_binary_tree(case)
        res = sol.sumNumbers(root)
        print(res)
