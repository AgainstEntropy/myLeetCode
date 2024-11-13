# 岛屿的最大面积
# Max Area of Island

from common import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area


if __name__ == "__main__":
    test_cases = [
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        [[0, 0, 0, 0, 0, 0, 0, 0]],
    ]
    sol = Solution()
    for case in test_cases:
        res = sol.maxAreaOfIsland(case)
        print(res)
