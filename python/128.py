# 最长连续序列
# Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 in num_set:
                continue

            curr_len = 1
            curr_num = num
            while curr_num + 1 in num_set:
                curr_len += 1
                curr_num += 1

            if curr_len > max_len:
                max_len = curr_len

        return max_len


if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2],),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],),
        ([1],),
        ([],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.longestConsecutive(*case)
        print(case, "\n", res)
