# Find First and Last Position of Element in Sorted Array
# 在排序数组中查找元素的第一个和最后一个位置


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        n = len(nums)
        if n == 0: return res
        
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                r = m
            elif nums[m] > target:
                r = m - 1
            else:  # nums[m] < target
                l = m + 1
        else:
            if nums[l] == target:
                res[0] = l
            else:
                return [-1, -1]
        
        r = n - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] == target:
                l = m
            elif nums[m] < target:
                l = m + 1
            else:  # nums[m] > target
                r = m - 1
        
        res[1] = l
        return res
        

if __name__ == '__main__':
    test_cases = [
        ([5,7,7,8,8,10], 8),
        ([5,7,7,8,8,10], 7),
        ([5,7,7,8,8,10], 6),
        ([], 0),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.searchRange(*case)
        print(case, '\n', res)