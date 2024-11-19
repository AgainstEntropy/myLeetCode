# 下一个排列
# Next Permutation

from common import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        left = n - 1
        while left > 0:
            if nums[left] > nums[left - 1]:
                break
            left -= 1

        if left == 0:
            self.sort(nums, 0, n)

        replace_index = left
        for i in range(left, n):
            if nums[left - 1] < nums[i] < nums[replace_index]:
                replace_index = i

        nums[left - 1], nums[replace_index] = nums[replace_index], nums[left - 1]

        self.sort(nums, left, n)

    @staticmethod
    def sort(nums: List[int], left: int, right: int) -> None:
        nums[left: right] = sorted(nums[left: right])


if __name__ == "__main__":
    test_cases = [
        [1, 4, 3, 2],
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
    ]

    sol = Solution()
    for nums in test_cases:
        sol.nextPermutation(nums)
        print(nums)
