// Kth Largest Element in an Array
// 数组中的第K个最大元素

#include "common.h"

class Solution
{
public:
    int findKthLargest(std::vector<int> &nums, int k)
    {
        std::priority_queue<int> max_heap;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (i < k)
            {
                max_heap.emplace(-nums[i]);
            }
            else if (-nums[i] < max_heap.top())
            {
                max_heap.pop();
                max_heap.emplace(-nums[i]);
            }
        }
        return -max_heap.top();
    }
};

int main()
{
    std::vector<std::tuple<std::vector<int>, int>> test_cases = {
        {{3, 2, 1, 5, 6, 4}, 2},
        {{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4},
    };

    Solution sol;
    for (auto &[nums, k] : test_cases)
    {
        int res = sol.findKthLargest(nums, k);
        std::cout << res << std::endl;
    }
}
