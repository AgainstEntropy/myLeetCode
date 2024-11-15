# 打家劫舍
# House Robber

from common import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * (n + 1)
        dp[1:3] = nums[:2]

        ans = max(dp[:3])
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i - 1]
            ans = max(dp[i], ans)

        return ans


if __name__ == "__main__":
    test_cases = [
        [2, 1, 1, 2],
        [1, 3, 1],
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
    ]

    for nums in test_cases:
        print(Solution().rob(nums))
