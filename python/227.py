# 基本计算器 II
# Basic Calculator II


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        num_stack: list[int] = []
        sign_stack: list[int] = []

        if s[0] != "-":
            s = "+" + s

        idx = 0
        while idx < len(s):

            if s[idx] not in "+-*/":
                num, idx = self.get_next_num(s, idx)
                num_stack.append(num)
                continue

            sign = s[idx]
            if sign == "+":
                sign_stack.append(1)
                idx += 1
            elif sign == "-":
                sign_stack.append(-1)
                idx += 1
            elif sign == "*":
                num, idx = self.get_next_num(s, idx + 1)
                num_prev = num_stack.pop()
                num_stack.append(num_prev * num)
            elif sign == "/":
                num, idx = self.get_next_num(s, idx + 1)
                num_prev = num_stack.pop()
                num_stack.append(num_prev // num)

        return sum(n * s for n, s in zip(num_stack, sign_stack))

    @staticmethod
    def get_next_num(s: str, idx: int) -> tuple[int, int]:
        num = ""
        while idx < len(s) and s[idx] not in "+-*/":
            num += s[idx]
            idx += 1

        return int(num), idx


if __name__ == "__main__":
    test_cases = [
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        (" - 2 * 4 + 2 / 2", -7),
        ("0", 0),
        (" - 0", 0),
    ]

    for s, expected in test_cases:
        print(Solution().calculate(s))
