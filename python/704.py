# Binary Search
# 二分查找


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:  # nums[m] > target
                r = m - 1
        
        return -1


if __name__ == '__main__':
    test_cases = [
        ([-1,0,3,5,9,12], 9),
        ([-1,0,3,5,9,12], 2),
        ([5], 5),
        ([5], -5),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.search(*case)
        print(case, '\n', res)