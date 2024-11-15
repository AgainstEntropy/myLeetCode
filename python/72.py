# 编辑距离
# Edit Distance


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[_] + [0] * m for _ in range(n + 1)]
        dp[0] = list(range(m + 1))

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0 and (word1[i] != word2[j]):
                    dp[i + 1][j + 1] = 1
                    continue

                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(
                        dp[i][j],       # replace
                        dp[i][j + 1],   # remove
                        dp[i + 1][j]    # insert
                    ) + 1

        return dp[-1][-1]


if __name__ == "__main__":
    test_cases = [
        ("horse", "ros"),
        ("intention", "execution"),
    ]

    for word1, word2 in test_cases:
        print(Solution().minDistance(word1, word2))
