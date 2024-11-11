# 最长公共前缀
# Longest Common Prefix

from common import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]

        common_prefix = ""
        min_length = min([len(s) for s in strs])

        for i in range(min_length):
            char_candidate = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != char_candidate:
                    return common_prefix

            common_prefix += char_candidate

        return common_prefix


if __name__ == "__main__":
    test_cases = [
        (["flower", "flow", "flight"],),
        (["dog", "racecar", "car"],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.longestCommonPrefix(*case)
        print(case, "\n", res)
