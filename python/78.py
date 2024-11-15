# 子集
# Subsets

from common import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            ans.extend([s + [num] for s in ans])

        return ans


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [0],
    ]

    for nums in test_cases:
        print(Solution().subsets(nums))
