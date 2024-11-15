# 最大正方形
# Maximal Square

from common import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        max_len = 0

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    dp[i + 1][j + 1] = 0
                else:
                    nabors = (dp[i][j], dp[i + 1][j], dp[i][j + 1])
                    nabor_max = max(nabors)
                    nabor_min = min(nabors)
                    if any([x == 0 for x in nabors]):
                        dp[i + 1][j + 1] = 1
                    elif any([x != nabor_max for x in nabors]):
                        dp[i + 1][j + 1] = nabor_min + 1
                    else:
                        dp[i + 1][j + 1] = nabor_max + 1

                max_len = max(max_len, dp[i + 1][j + 1])

        return max_len**2


if __name__ == "__main__":
    test_cases = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
        ],
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        [
            ["0", "1"],
            ["1", "0"],
        ],
        [["0"]],
    ]

    for matrix in test_cases:
        print(Solution().maximalSquare(matrix))
