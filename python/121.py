# 买卖股票的最佳时机
# Best Time to Buy and Sell Stock

from common import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p

            if (profit := p - min_price) > max_profit:
                max_profit = profit

        return max_profit


if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
    ]
    for prices in test_cases:
        print(Solution().maxProfit(prices))
