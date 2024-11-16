# Find the Power of K-Size Subarrays I

from common import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        diff = [nums[i] - nums[i - 1] for i in range(1, n)]

        ans = []

        count = {}
        for i in range(k - 1):
            count[diff[i]] = count.get(diff[i], 0) + 1

        for i in range(k - 1, n - 1):
            ans.append(nums[i] if count.get(1, 0) == k - 1 else -1)

            count[diff[i]] = count.get(diff[i], 0) + 1
            count[diff[i - k + 1]] -= 1

        ans.append(nums[n - 1] if count.get(1, 0) == k - 1 else -1)

        return ans


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 3, 2, 5], 3),
        ([2, 2, 2, 2, 2], 4),
        ([3, 2, 3, 2, 3, 2], 2),
    ]

    sol = Solution()
    for test_case in test_cases:
        print(sol.resultsArray(*test_case))
