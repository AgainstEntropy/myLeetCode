# Find Peak Element
# 寻找峰值


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return l


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 1],),
        ([1, 2, 1, 3, 5, 6, 4],),
        ([1],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.findPeakElement(*case)
        print(case, '\n', res)