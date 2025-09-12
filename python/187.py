# Repeated DNA Sequences
# 重复的DNA序列


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seq_count = {}
        length = 10

        results = set()

        for i in range(len(s) - length + 1):
            sub_seq = s[i : i + length]
            count = seq_count.get(sub_seq, 0)
            if count == 1:
                results.add(sub_seq)
            seq_count[sub_seq] = count + 1

        return list(results)


if __name__ == "__main__":
    test_cases = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA",
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.findRepeatedDnaSequences(case))
