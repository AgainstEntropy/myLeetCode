# Two Sum
# 两数之和


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        comp_dict = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in comp_dict:
                return [comp_dict[comp], i]
            comp_dict[num] = i
        return []

if __name__ == '__main__':
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.twoSum(*case)
        print(case, '\n', res)