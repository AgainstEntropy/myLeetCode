// 最长连续序列
// Longest Consecutive Sequence

#include "common.h"
#include <unordered_map>

class Solution
{
public:
    int longestConsecutive(std::vector<int> &nums)
    {
        std::unordered_map<int, bool> num_set;
        for (int num : nums)
        {
            num_set[num] = true;
        }
        int max_len = 0;

        for (auto &[num, _] : num_set)
        {
            if (num_set.find(num - 1) != num_set.end())
            {
                continue;
            }

            int curr_len = 1;
            int curr_num = num;
            while (num_set.find(curr_num + 1) != num_set.end())
            {
                curr_len += 1;
                curr_num += 1;
            }
            max_len = std::max(max_len, curr_len);
        }
        return max_len;
    }
};

int main()
{
    std::vector<std::vector<int>> test_cases = {
        {100, 4, 200, 1, 3, 2},
        {0, 3, 7, 2, 5, 8, 4, 6, 0, 1},
        {1},
        {},
    };

    Solution sol;
    for (auto &nums : test_cases)
    {
        int res = sol.longestConsecutive(nums);
        std::cout << res << std::endl;
    }
}
