# Spiral Matrix
# 螺旋矩阵


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        out = []
        rmin, rmax = 0, len(matrix)-1
        cmin, cmax = 0, len(matrix[0])-1
    
        while True:
            for ccur in range(cmin, cmax+1):
                out.append(matrix[rmin][ccur])
            rmin += 1
            if rmin > rmax: break

            for rcur in range(rmin, rmax+1):
                out.append(matrix[rcur][cmax])
            cmax -= 1
            if cmax < cmin: break
                    
            for ccur in range(cmax, cmin-1, -1):
                out.append(matrix[rmax][ccur])
            rmax -= 1
            if rmax < rmin: break
                    
            for rcur in range(rmax, rmin-1, -1):
                out.append(matrix[rcur][cmin])
            cmin += 1
            if cmin > cmax: break
                    
        return out
    

if __name__ == '__main__':
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]],),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.spiralOrder(*case)
        print(case, '\n', res)