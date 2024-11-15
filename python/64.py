# 最小路径和
# Minimum Path Sum

from common import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i + 1][j + 1] = dp[i + 1][j] + grid[i][j]
                elif j == 0:
                    dp[i + 1][j + 1] = dp[i][j + 1] + grid[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]

        return dp[-1][-1]


if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1],
            ]
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        ),
    ]

    for grid in test_cases:
        print(Solution().minPathSum(grid))
