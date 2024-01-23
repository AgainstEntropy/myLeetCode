# Find Minimum in Rotated Sorted Array
# 寻找旋转排序数组中的最小值


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[l]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                break
        return nums[l]


if __name__ == '__main__':
    test_cases = [
        ([3,4,5,1,2],),
        ([4,5,6,7,0,1,2],),
        ([11,13,15,17],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.findMin(*case)
        print(case, '\n', res)