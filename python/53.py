# 最大子数组和
# Maximum Subarray

from common import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        curr_sum = 0
        for num in nums:
            maxSum = max(maxSum, curr_sum := max(curr_sum, 0) + num)

        return maxSum


if __name__ == "__main__":
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
    ]

    sol = Solution()

    for nums in test_cases:
        print(sol.maxSubArray(nums))
