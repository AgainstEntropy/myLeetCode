# Minimum Window Substring
# 最小覆盖子串


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_chars = dict()
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        satisfied_chars = set()
        left, right = 0, 0
        min_len = len(s) + 1
        window_chars = dict()
        while right < len(s):
            right_char = s[right]

            if right_char in t_chars:
                window_chars[right_char] = window_chars.get(right_char, 0) + 1
                if window_chars[right_char] == t_chars[right_char]:
                    satisfied_chars.add(right_char)

            while len(satisfied_chars) == len(t_chars):
                length = right - left + 1
                if length < min_len:
                    min_len = length
                    min_window = s[left:right+1]

                left_char = s[left]
                left += 1

                if left_char in t_chars:
                    window_chars[left_char] -= 1
                    if window_chars[left_char] < t_chars[left_char]:
                        satisfied_chars.remove(left_char)

            right += 1
        
        return min_window if min_len != len(s) + 1 else ""


if __name__ == '__main__':
    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("a", "b"),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.minWindow(*case)
        print(case, '\n', res)