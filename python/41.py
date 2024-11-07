# 缺失的第一个正整数
# First Missing Positive


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while (1 <= nums[i] <= n) and (nums[i] != nums[nums[i] - 1]):
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0],),
        ([3, 4, -1, 1],),
        ([7, 8, 9, 11, 12],),
        ([1],),
        ([2],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.firstMissingPositive(*case)
        print(case, "\n", res)
