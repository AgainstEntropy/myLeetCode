// 滑动窗口最大值
// Sliding Window Maximum

#include "common.h"

class Solution
{
public:
    std::vector<int> maxSlidingWindow(std::vector<int> &nums, int k)
    {
        std::priority_queue<std::pair<int, int>> max_heap;
        for (int i = 0; i < k; ++i)
        {
            max_heap.emplace(nums[i], i);
        }
        std::vector<int> result = {max_heap.top().first};

        for (int i = k; i < nums.size(); ++i)
        {
            max_heap.emplace(nums[i], i);
            while (max_heap.top().second <= i - k)
            {
                max_heap.pop();
            }
            result.push_back(max_heap.top().first);
        }
        return result;
    }
};

int main()
{
    std::vector<std::tuple<std::vector<int>, int>> test_cases = {
        {{1, 3, -1, -3, 5, 3, 6, 7}, 3},
        {{1}, 1},
    };

    for (auto &[nums, k] : test_cases)
    {
        print_vector(Solution().maxSlidingWindow(nums, k));
    }
    return 0;
}