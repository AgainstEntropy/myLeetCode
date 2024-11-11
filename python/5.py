# 最长回文子串
# Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        max_start, max_len = 0, 1
        dp = [[False,] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                    if dp[i][j] and (j - i + 1) > max_len:
                        max_len = j - i + 1
                        max_start = i

        return s[max_start: max_start + max_len]


if __name__ == "__main__":
    test_cases = [
        ("aacabdkacaa",),
        ("ac",),
        ("babad",),
        ("cbbd",),
        ("a",),
        ("",),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.longestPalindrome(*case)
        print(case, "\n", res)
