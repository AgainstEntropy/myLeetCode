# 验证IP地址
# Validate IP Address


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP and ":" not in queryIP:
            if self.varifyIPv4(queryIP):
                return "IPv4"
        elif ":" in queryIP and "." not in queryIP:
            if self.varifyIPv6(queryIP):
                return "IPv6"

        return "Neither"

    @staticmethod
    def varifyIPv4(queryIP: str) -> bool:
        parts = queryIP.split(".")
        if len(parts) != 4:
            return False

        for part in parts:
            if len(part) == 0:
                return False
            if part[0] == "0" and len(part) > 1:
                return False

            try:
                if not 0 <= int(part) <= 255:
                    return False
            except:
                return False

        return True

    @staticmethod
    def varifyIPv6(queryIP: str) -> bool:
        parts = queryIP.split(":")
        if len(parts) != 8:
            return False

        for part in parts:
            if not 1 <= len(part) <= 4:
                return False

            for digit in part:
                if not digit.isdigit() and digit not in "abcdefABCDEF":
                    return False

        return True


if __name__ == "__main__":
    test_cases = [
        "2001:0db8:85a3:0:0:8A2E:0370:7334",
        "172.16.254.1",
        "256.256.256.256",
        "192.168.01.1",
    ]

    sol = Solution()
    for queryIP in test_cases:
        print(sol.validIPAddress(queryIP))
