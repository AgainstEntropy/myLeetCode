# 乘积最大子数组
# Maximum Product Subarray

from common import List


class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        max_prod = nums[-1]

        prods = [nums[-1]]

        for num in reversed(nums[: len(nums) - 1]):
            prods = [num * p for p in [1] + prods]
            max_prod = max(max_prod, max(prods))

        return max_prod

    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod = nums[0], nums[0]

        ans = max_prod

        for num in nums[1:]:
            max_temp, min_temp = max_prod, min_prod
            max_prod = max(max_temp * num, num, min_temp * num)
            min_prod = min(min_temp * num, num, max_temp * num)
            ans = max(max_prod, ans)

        return ans


if __name__ == "__main__":
    test_cases = [
        [1, 0, -5, 2, 3, -8, -9],
        [-2],
        [0, 2],
        [2, 3, -2, 4],
        [-2, 0, -1],
    ]

    for nums in test_cases:
        print(Solution().maxProduct(nums))
