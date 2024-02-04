# 3Sum
# 三数之和


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        solutions = []
        if nums[0] > 0 or nums[-1] < 0: return solutions

        for i, num in enumerate(nums[:n-2]):
            if num > 0: break
            elif num == 0 and nums[i+1] > 0: break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                while left < right and (left > i + 1) and nums[left-1] == nums[left]:
                    left += 1
                while left < right and (right < n - 1) and nums[right] == nums[right+1]:
                    right -= 1
                sum_ = num + nums[left] + nums[right]
                if left < right and sum_ == 0:
                    solutions.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
        return solutions


if __name__ == '__main__':
    test_cases = [
        ([-1,0,1,2,-1,-4,-2,-3,3,0,4],),
        ([-1, 0, 1, 2, -1, -4],),
        ([0, 1, 1],),
        ([0, 0, 0],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.threeSum(*case)
        print(case, '\n', res)