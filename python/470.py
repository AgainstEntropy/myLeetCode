# 用 Rand7() 实现 Rand10()
# Implement Rand10() Using Rand7()


import random


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        return 5 * self.rand2() + self.rand5()

    @staticmethod
    def rand2():
        while (res := rand7()) > 6:
            continue
        return res % 2

    @staticmethod
    def rand5():
        while (res := rand7()) >= 6:
            continue
        return res


if __name__ == "__main__":
    test_cases = [1, 2, 3]

    sol = Solution()
    for times in test_cases:
        print([sol.rand10() for _ in range(times)])
