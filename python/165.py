# 比较版本号
# Compare Version Numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = [int(rev) for rev in version1.split(".")]
        v2_list = [int(rev) for rev in version2.split(".")]

        max_len = max(len(v1_list), len(v2_list))
        v1_list.extend([0] * (max_len - len(v1_list)))
        v2_list.extend([0] * (max_len - len(v2_list)))

        for rev1, rev2 in zip(v1_list, v2_list):
            if rev1 < rev2:
                return -1
            if rev1 > rev2:
                return 1

        return 0


if __name__ == "__main__":
    test_cases = [
        ("1.2", "1.10"),
        ("2.11", "2.02"),
        ("1.01", "1.001"),
        ("1.0", "1.0.0.0"),
    ]

    sol = Solution()
    for version1, version2 in test_cases:
        print(sol.compareVersion(version1, version2))
