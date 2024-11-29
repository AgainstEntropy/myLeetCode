# Rotating the Box

from common import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        res = [["."] * m for _ in range(n)]

        for i in range(m):
            row = boxGrid[i]
            _m = m - 1 - i

            slow = fast = n - 1
            while fast >= 0:
                while fast >= 0 and row[fast] == "*":
                    res[fast][_m] = "*"
                    fast -= 1
                if fast < 0:
                    break
                slow = fast

                # count stones between two obstacle
                count = 0
                while fast >= 0 and row[fast] != "*":
                    if row[fast] == "#":
                        count += 1
                    fast -= 1

                # fill in stones in the rotated box
                while count > 0:
                    res[slow][_m] = "#"
                    count -= 1
                    slow -= 1

        return res


if __name__ == "__main__":
    test_cases = [
        ([["#", ".", "#"]], [["."], ["#"], ["#"]]),
        (
            [
                ["#", ".", "*", "."],
                ["#", "#", "*", "."],
            ],
            [
                ["#", "."],
                ["#", "#"],
                ["*", "*"],
                [".", "."],
            ],
        ),
        (
            [
                ["#", "#", "*", ".", "*", "."],
                ["#", "#", "#", "*", ".", "."],
                ["#", "#", "#", ".", "#", "."],
            ],
            [
                [".", "#", "#"],
                [".", "#", "#"],
                ["#", "#", "*"],
                ["#", "*", "."],
                ["#", ".", "*"],
                ["#", ".", "."],
            ],
        ),
    ]

    sol = Solution()
    for boxGrid, expected in test_cases:
        res = sol.rotateTheBox(boxGrid)
        print(res == expected, "\n", res)
