# Move Zeroes
# 移动零


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow, fast = 0, 0
        while fast < n - 1:
            fast += 1
            if nums[fast] != 0:
                while nums[slow] != 0 and slow < fast:
                    slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

if __name__ == '__main__':
    test_cases = [
        [2, 1, 3, 0, 1],
        [2, 1],
        [0, 1, 0, 3, 12],
        [0, 0, 1, 0, 3, 12, 0],
        [0],
    ]

    sol = Solution()
    for case in test_cases:
        print(case)
        res = sol.moveZeroes(case)
        print(case)
