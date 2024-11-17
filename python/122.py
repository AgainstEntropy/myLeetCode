# 买卖股票的最佳时机 II
# Best Time to Buy and Sell Stock II

from common import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
    ]

    sol = Solution()
    for prices in test_cases:
        print(sol.maxProfit(prices))
