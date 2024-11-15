# 删除最短子数组使剩余数组有序
# Shortest Subarray to be Removed to Make Array Sorted

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        right = n - 1
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1

        ans = min(n - left - 1, right)

        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans


if __name__ == "__main__":
    test_cases = [
        [2, 2, 2, 1, 1, 1],
        [13, 0, 14, 7, 18, 18, 18, 16, 8, 15, 20],
        [1, 2, 3, 10, 4, 2, 3, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 3],
    ]

    sol = Solution()

    for arr in test_cases:
        print(sol.findLengthOfShortestSubarray(arr))
