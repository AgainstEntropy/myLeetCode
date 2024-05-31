# TMaximum Length of Repeated Subarray
# 最长重复子数组


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp_matrix = [[0] * (m + 1) for _ in range(n + 1)]

        res = 0

        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp_matrix[i + 1][j + 1] = dp_matrix[i][j] + 1

                if dp_matrix[i + 1][j + 1] > res:
                    res = dp_matrix[i + 1][j + 1]
        return res


if __name__ == '__main__':
    test_cases = [
        ([1,0,0,0,1], [1,0,0,1,1]),
        ([1,2,3,2,1], [3,2,1,4,7]),
        ([1,2,3,2,1], [3,2,1,2,3]),
        ([1,2,3,2,1], [1,1,1,1,1]),
        ([0,0,0,0,0], [0,0,0,0,0]),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.findLength(*case)
        print(case, '\n', res)