# 复原 IP 地址
# Restore IP Addresses

from common import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans: list[str] = []
        stack: list[int] = [0]

        def backtrack(num_sep: int, start_index: int):
            if num_sep == 3:
                if n - stack[-1] > 3:
                    return
                if self.validate(s[stack[-1] :]):
                    ans.append(self.ip_from_sep(s, stack + [n + 1]))

                return

            for i in range(start_index, min(start_index + 3, n + num_sep - 2)):
                if i - stack[-1] > 3:
                    return
                if self.validate(s[stack[-1] : i]):
                    stack.append(i)
                    backtrack(num_sep + 1, max(stack[-1] + 1, n - (2 - num_sep) * 3))
                    stack.pop()

        num_sep = 0
        backtrack(num_sep, max(1, n - (3 - num_sep) * 3))

        return ans

    @staticmethod
    def validate(s: str) -> bool:
        return s == "0" or (not s.startswith("0") and 0 <= int(s) <= 255)

    @staticmethod
    def ip_from_sep(s: str, sep: list[int]) -> str:
        return ".".join(s[sep[i] : sep[i + 1]] for i in range(len(sep) - 1))


if __name__ == "__main__":
    test_cases = [
        "101023",
        "0000",
        "25525511135",
    ]

    sol = Solution()

    for s in test_cases:
        print(sol.restoreIpAddresses(s))
