# Sqrt(x)
# x 的平方根


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            m = (l + r) // 2
            if m ** 2 < x:
                l = m + 1
            else:
                r = m

        if l ** 2 > x:
            return l - 1

        return l
    
if __name__ == '__main__':
    test_cases = [
        (4,),
        (8,),
        (9,),
        (16,),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.mySqrt(*case)
        print(case, '\n', res)