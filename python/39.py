# Combination Sum
# 组合总和


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        def backtrack(total, start_index):
            if total > target:
                return

            if total == target:
                res.append(path[:])
                return

            for i in range(start_index, len(candidates)):
                if total + candidates[i] > target:
                    break

                total += candidates[i]
                path.append(candidates[i])
                backtrack(total, i)
                total -= candidates[i]
                path.pop()
        candidates.sort()
        backtrack(0, 0)
        return res


if __name__ == '__main__':
    test_cases = [
        ([2,3,6,7], 7),
        ([2,3,5], 8),
        ([2], 1),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.combinationSum(*case)
        print(case, '\n', res)