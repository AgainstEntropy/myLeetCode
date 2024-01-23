# Median of Two Sorted Arrays
# 寻找两个正序数组的中位数


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        l, r = 0, n1
        while l < r:
            m = (l + r) // 2
            if nums1[m] < nums2[k - m - 1]:
                l = m + 1
            else:
                r = m

        m1 = l
        m2 = k - m1
        
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1], float('-inf') if m2 <= 0 else nums2[m2 - 1])
        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(float('inf') if m1 >= n1 else nums1[m1], float('inf') if m2 >= n2 else nums2[m2])
        return (c1 + c2) / 2


if __name__ == '__main__':
    test_cases = [
        ([1, 3], [2]),
        ([3], [-2, -1]),
        ([], [2, 3]),
        ([0, 1, 2, 3], [0, 1, 2, 3, 4]),
        ([1, 2], [3, 4]),
        ([0, 0], [0, 0]),
        ([], [1]),
        ([2], []),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.findMedianSortedArrays(*case)
        print(case, '\n', res)