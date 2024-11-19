# 字符串转换整数 (atoi)
# String to Integer (atoi)

MAX = 2**31


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        nums = []

        negative = False

        i = 0
        for i, digit in enumerate(s):
            if i == 0:
                if digit in "+-":
                    negative = digit == "-"
                    continue
            if digit.isdigit():
                nums.append(int(digit))
            else:
                break

        num = 0
        for digit in nums:
            num *= 10
            num += digit

        if negative:
            num = -num

        if num < -MAX:
            return -MAX
        if num > MAX - 1:
            return MAX - 1

        return num


if __name__ == "__main__":
    test_cases = [
        "-91283472332",
        "91283472332",
        "42",
        "   -042",
        "   -00042",
        "1337c0d3",
        "0-1",
        "words and 987",
    ]

    sol = Solution()
    for s in test_cases:
        print(sol.myAtoi(s))
