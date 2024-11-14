# 爬楼梯
# Climbing Stairs


from functools import lru_cache


class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for n in test_cases:
        print(Solution().climbStairs(n))
