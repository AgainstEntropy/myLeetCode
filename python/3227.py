# Vowels Game in a String
# 字符串元音游戏


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        for c in s:
            if c in vowels:
                return True

        return False


if __name__ == "__main__":
    test_cases = ["leetcoder", "bbcd", "ifld", "sloalo"]

    sol = Solution()
    for case in test_cases:
        print(sol.doesAliceWin(case))
