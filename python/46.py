# 全排列
# Permutations

from common import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans: list[list[int]] = [[nums[0]]]

        if n == 1:
            return ans

        for idx, num in enumerate(nums[1:]):
            all_pos = list(range(idx + 2))
            to_insert = [num]
            ans = [x[:p] + to_insert + x[p:] for x in ans for p in all_pos]

        return ans


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]

    sol = Solution()

    for nums in test_cases:
        print(sol.permute(nums))
