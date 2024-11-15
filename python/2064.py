# Minimized Maximum of Products Distributed to Any Store

from common import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def canDistribute(max_quantity: int) -> bool:
            n_stores = [(q + max_quantity - 1) // max_quantity for q in quantities]
            return sum(n_stores) <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    test_cases = [
        (2, [5, 7]),
        (6, [11, 6]),
        (7, [15, 10, 10]),
        (7, [16, 10, 10]),
        (1, [100000]),
    ]

    for n, quantities in test_cases:
        print(Solution().minimizedMaximum(n, quantities))
