# Largest Number
# 最大数


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        from functools import cmp_to_key
        def order(a, b):
            if a+b > b+a:
                return 1
            elif a+b == b+a:
                return 0
            else:
                return -1
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(order), reverse=True)
        return str(int(''.join(nums_str)))
    

if __name__ == '__main__':
    test_cases = [
        ([10,2],),
        ([3,30,34,5,9],),
        ([1],),
        ([10],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.largestNumber(*case)
        print(case, '\n', res)