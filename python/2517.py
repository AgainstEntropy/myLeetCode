# Count Unguarded Cells in the Grid

from common import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]

        count = 0
        for y, x in guards + walls:
            grid[y][x] = 1
            count += 1

        for y, x in guards:
            for i in range(x - 1, -1, -1):
                if grid[y][i] > 0:
                    break
                count += grid[y][i] == 0
                grid[y][i] = -1
            for i in range(x + 1, n):
                if grid[y][i] > 0:
                    break
                count += grid[y][i] == 0
                grid[y][i] = -1
            for j in range(y - 1, -1, -1):
                if grid[j][x] > 0:
                    break
                count += grid[j][x] == 0
                grid[j][x] = -1
            for j in range(y + 1, m):
                if grid[j][x] > 0:
                    break
                count += grid[j][x] == 0
                grid[j][x] = -1

        return m * n - count


if __name__ == "__main__":
    test_cases = [
        (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]),
        (3, 3, [[1, 1]], [[0, 1], [1, 0], [1, 2], [2, 1]]),
    ]

    sol = Solution()
    for m, n, guards, walls in test_cases:
        print(sol.countUnguarded(m, n, guards, walls))
