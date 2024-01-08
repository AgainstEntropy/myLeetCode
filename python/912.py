# Sort an Array
# 排序数组


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1: return nums

        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)
    
    @staticmethod
    def merge(left: list[int], right: list[int]) -> list[int]:
        m, n = len(left), len(right)
        idx1 = m - 1
        idx2 = n - 1
        idx = m + n - 1

        left.extend([0] * n)
        while (idx1 >= 0 and idx2 >= 0):
            if left[idx1] > right[idx2]:
                left[idx] = left[idx1]
                idx -= 1
                idx1 -= 1
            else:
                left[idx] = right[idx2]
                idx -= 1
                idx2 -= 1
            
        if idx1 < 0:
            left[:idx2+1] = right[:idx2+1]

        return left
    

if __name__ == '__main__':
    test_cases = [
        [5,2,3,1],
        [5,1,1,2,0,0],
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.sortArray(case)
        print(case, '\n', res)