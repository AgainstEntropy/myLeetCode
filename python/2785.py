# Sort Vowels in a String
# 将字符串中的元音字母排序


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowels_chars, vowels_indices = [], []
        for i, c in enumerate(s):
            if c in vowels:
                vowels_indices.append(i)
                vowels_chars.append(c)

        vowels_chars = sorted(vowels_chars)

        result = list(s)
        for i, ii in enumerate(vowels_indices):
            result[ii] = vowels_chars[i]

        return "".join(result)


if __name__ == "__main__":
    test_cases = [
        "lEetcOde",
        "lYmpH",
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.sortVowels(case))
