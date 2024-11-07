# 有效的括号
# Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        stack = [s[0]]

        right_to_left = {")": "(", "]": "[", "}": "{"}

        for c in s[1:]:
            if not stack or c not in right_to_left:
                stack.append(c)
            elif stack[-1] == right_to_left[c]:
                stack.pop()
            else:
                return False

        return not stack


if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("[", False)
    ]

    for s, expected in test_cases:
        print(Solution().isValid(s))
