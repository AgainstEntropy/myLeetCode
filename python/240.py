# Search a 2D Matrix II
# 搜索二维矩阵 II


class Solution:
    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        n_row = len(matrix)
        for row in range(n_row):
            if matrix[row][0] > target:
                break
            if matrix[row][-1] < target:
                continue
            l, r = 0, len(matrix[row]) - 1
            while l < r:
                m = (l + r) // 2
                if matrix[row][m] < target:
                    l = m + 1
                elif matrix[row][m] > target:
                    r = m - 1
            if matrix[row][l] == target:
                return True
        return False
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])

        # search the diagonal
        l, r = 0, min(n_row, n_col) - 1
        while l < r:
            m = (l + r) // 2
            if matrix[m][m] < target:
                l = m + 1
            else:
                r = m
        if matrix[l][l] == target:
            return True
            
        # all elements on the right or below of the l-th diagonal are larger than target
        # search rows and cols on the left and above of the l-th diagonal
        for i in range(l + 1):
            # search row i
            left, right = 0, n_col - 1
            while left < right:
                mid = (left + right) // 2
                if matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if matrix[i][left] == target:
                return True
                
            # search col i
            up, down = 0, n_row - 1
            while up < down:
                mid = (up + down) // 2
                if matrix[mid][i] < target:
                    up = mid + 1
                else:
                    down = mid
            if matrix[up][i] == target:
                return True
        
        return False


if __name__ == '__main__':
    test_cases = [
        ([[1, 2]], 2),
        ([[-5]], -5),
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]], 12),
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5),
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20),
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 100),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.searchMatrix(*case)
        print(case, '\n', res)