# Take K of Each Character From Left and Right


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        n = len(s)
        count = {"a": 0, "b": 0, "c": 0}

        statisfied = 0
        left = 0
        while left < n:
            count[s[left]] += 1
            if count[s[left]] == k:
                statisfied += 1
                if statisfied == 3:
                    break
            left += 1
        else:
            return -1

        right = 0
        min_minutes = left + right + 1
        for left in range(left, -1, -1):
            c = s[left]
            count[c] -= 1
            while count[c] < k:
                right += 1
                count[s[-right]] += 1
            min_minutes = min(min_minutes, left + right)

        return min_minutes


if __name__ == "__main__":
    test_cases = [
        ("a", 0),
        ("abaabbbbc", 1),
        ("aabaaaacaabc", 2),
        ("abc", 1),
        ("a", 1),
    ]

    sol = Solution()
    for s, k in test_cases:
        print(sol.takeCharacters(s, k))
