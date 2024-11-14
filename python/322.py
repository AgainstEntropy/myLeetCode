# 零钱兑换
# Coin Change

from common import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [-1] * (amount + 1)
        minCoins[0] = 0
        coins.sort()

        for i in range(amount + 1):
            for c in coins:
                if i + c <= amount and minCoins[i] != -1:
                    if minCoins[i + c] == -1 or minCoins[i + c] > minCoins[i] + 1:
                        minCoins[i + c] = minCoins[i] + 1

        return minCoins[amount]


if __name__ == "__main__":
    test_cases = [
        ([186, 419, 83, 408], 6249),
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
    ]
    for coins, amount in test_cases:
        print(Solution().coinChange(coins, amount))
