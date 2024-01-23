# Search in Rotated Sorted Array
# 搜索旋转排序数组


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        R = self.findMin(nums)
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            mm = (m + R) % n
            if nums[mm] == target:
                return mm
            elif nums[mm] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

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
        return l


if __name__ == '__main__':
    test_cases = [
        ([4,5,6,7,0,1,2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.search(*case)
        print(case, '\n', res)