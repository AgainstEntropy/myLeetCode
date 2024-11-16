# 括号生成
# Generate Parentheses

from common import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def backtrack(count: int, index: int):
            if index == 2 * n:
                if count == 0:
                    ans.append("".join(stack))
            else:
                if count < n:
                    stack.append("(")
                    backtrack(count + 1, index + 1)
                    stack.pop()
                if count > 0:
                    stack.append(")")
                    backtrack(count - 1, index + 1)
                    stack.pop()

        backtrack(0, 0)

        return ans


if __name__ == "__main__":
    test_cases = [
        (1, ["()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
    ]

    sol = Solution()
    for n, expected in test_cases:
        ans = sol.generateParenthesis(n)
        print(sorted(ans) == sorted(expected))
        print(sorted(ans))
        print(sorted(expected))
