# 最长递增子序列
# Longest Increasing Subsequence

from common import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    test_cases = [
        [1, 3, 6, 7, 9, 4, 10, 5, 6],
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
    ]
    for nums in test_cases:
        print(Solution().lengthOfLIS(nums))
