# 岛屿数量
# Number of Islands

from common import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0

        def dfs(i: int, j: int):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands


if __name__ == "__main__":
    test_cases = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
    ]
    sol = Solution()
    for case in test_cases:
        res = sol.numIslands(case)
        print(res)
