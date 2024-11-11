# 字符串相乘
# Multiply Strings


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        if num1 == "1":
            return num2
        elif num2 == "1":
            return num1

        results = [self.multiply_with_1bit(num1, int(bit)) for bit in num2]
        factors = [10**i for i in range(len(results))]
        factors.reverse()

        return str(sum([a * b for a, b in zip(results, factors)]))

    @staticmethod
    def multiply_with_1bit(num1: str, bit: int) -> int:
        bits = [int(x) for x in num1[::-1]]

        results = []
        carry = 0
        for b1 in bits:
            res = b1 * bit + carry
            results.insert(0, res % 10)
            carry = res // 10

        if carry:
            results.insert(0, carry)

        factors = [10**i for i in range(len(results))]
        factors.reverse()

        return sum([a * b for a, b in zip(results, factors)])


if __name__ == "__main__":
    test_cases = [
        ("0", "123"),
        ("123", "0"),
        ("123", "1"),
        ("2", "3"),
        ("123", "456"),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.multiply(*case)
        print(case, "\n", res)
