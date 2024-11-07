# Longest Valid Parentheses
# 最长有效括号


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    stack.append(i)
        return ans


if __name__ == "__main__":
    test_cases = [
        (")((()))))", 6),
        ("(()", 2),
        (")()())", 4),
        (")()())()", 4),
    ]

    for s, expected in test_cases:
        ans = Solution().longestValidParentheses(s)
        print(f"longestValidParentheses({s}) = {ans}, answer is {ans == expected}")
