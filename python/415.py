# Add Strings
# 字符串相加


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        answer = []
        carry = 0
        i, j = len(num1), len(num2)
        if i < j:
            num1, num2 = num2, num1
            i, j = j, i
        num2 = '0' * (i - j) + num2

        d = 1
        while d < i+1:
            s = int(num1[-d]) + int(num2[-d]) + carry
            carry = s // 10
            answer.append(str(s % 10))
            d += 1
        if carry:
            answer.append('1')

        return ''.join(answer[::-1])


if __name__ == '__main__':
    test_cases = [
        ("11", "123"),
        ("456", "77"),
        ("0", "0"),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.addStrings(*case)
        print(case, '\n', res)