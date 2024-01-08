# Majority Element
# 多数元素


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for k, v in count.items():
            if v > len(nums)//2:
                return k
            

if __name__ == '__main__':
    test_cases = [
        ([3,2,3],),
        ([2,2,1,1,1,2,2],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.majorityElement(*case)
        print(case, '\n', res)