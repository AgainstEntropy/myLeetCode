# 翻转字符串中的单词
# Reverse Words in a String


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


if __name__ == "__main__":
    test_cases = [
        ("the sky is blue",),
        ("  hello world  ",),
        ("a",),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.reverseWords(*case)
        print(case, "\n", res)
