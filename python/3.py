# Longest Substring Without Repeating Characters
# 最长不重复子串


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        left, right = 0, 0
        max_len = 0
        chars = dict()
        while right < n:
            chars[s[right]] = chars.get(s[right], 0) + 1
            while chars[s[right]] > 1:
                chars[s[left]] -= 1
                left += 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
            right += 1

        return max_len


if __name__ == '__main__':
    test_cases = [
        ("abcabcbb",),
        ("bbbbb",),
        ("pwwkew",),
        ("",),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.lengthOfLongestSubstring(*case)
        print(case, '\n', res)