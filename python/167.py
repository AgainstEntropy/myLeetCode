# Two Sum II - Input Array Is Sorted
# 两数之和 II - 输入有序数组


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.twoSum(*case)
        print(case, '\n', res)