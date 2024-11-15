# 不同路径
# Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb

        return comb(m + n - 2, m - 1)


if __name__ == "__main__":
    test_cases = [
        (3, 2),
        (3, 7),
    ]

    for m, n in test_cases:
        print(Solution().uniquePaths(m, n))
