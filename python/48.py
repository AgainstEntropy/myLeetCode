# Rotate Image
# 旋转图像


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                    matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
                

if __name__ == '__main__':
    test_case = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
    ]

    sol = Solution()
    for case in test_case:
        print(case)
        res = sol.rotate(case)
        print(case, '\n')