# Single Number
# 只出现一次的数字


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            c = count.get(num, 0)
            if c:
                count.pop(num)
            else:
                count[num] = 1
        
        return list(count.keys())[0]
    

if __name__ == '__main__':
    test_cases = [
        [2,2,1],
        [4,1,2,1,2],
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.singleNumber(case)
        print(case, '\n', res)