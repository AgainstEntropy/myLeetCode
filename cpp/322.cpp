// 零钱兑换
// Coin Change

#include "common.h"
#include <algorithm>

struct Solution
{
    int coinChange(std::vector<int> &coins, int amount)
    {
        std::vector<int> minCoins(amount + 1, -1);
        minCoins[0] = 0;
        std::sort(coins.begin(), coins.end());

        for (int i = 0; i <= amount; i++)
        {
            for (int c : coins)
            {
                if (i + c <= amount && minCoins[i] != -1)
                {
                    if (minCoins[i + c] == -1 || minCoins[i + c] > minCoins[i] + 1)
                    {
                        minCoins[i + c] = minCoins[i] + 1;
                    }
                }
            }
        }
        return minCoins[amount];
    }
};

int main()
{
    Solution s;
    std::vector<std::tuple<std::vector<int>, int>> test_cases = {
        {{1, 2, 5}, 11},
        {{2}, 3},
        {{1}, 0},
    };
    for (auto &[coins, amount] : test_cases)
    {
        std::cout << s.coinChange(coins, amount) << std::endl;
    }
}
