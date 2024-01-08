# Merge Sorted Array
# 合并两个有序数组


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m - 1
        idx2 = n - 1
        idx = m + n - 1
        while (idx1 >= 0 and idx2 >= 0):
            if nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx -= 1
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx -= 1
                idx2 -= 1
            
        if idx1 < 0:
            nums1[:idx2+1] = nums2[:idx2+1]


if __name__ == '__main__':
    test_cases = [
        [[1,2,3,0,0,0], 3, [2,5,6], 3],
        [[1], 1, [], 0],
        [[0], 0, [1], 1],
    ]

    sol = Solution()
    for case in test_cases:
        print(case)
        res = sol.merge(*case)
        print(case, '\n')