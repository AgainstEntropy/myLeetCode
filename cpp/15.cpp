// 3Sum
// 三数之和

#include "common.h"
#include <algorithm>

class Solution
{
public:
    std::vector<std::vector<int>> threeSum(std::vector<int> &nums)
    {
        std::vector<std::vector<int>> results;

        std::sort(nums.begin(), nums.end());
        int n = nums.size();

        if (nums[0] > 0 || nums[n - 1] < 0)
        {
            return results;
        }

        int num, sum;
        int left, right;
        for (int i = 0; i < n - 2; ++i)
        {
            num = nums[i];
            if (num > 0 || (num == 0 && nums[i + 1] > 0))
            {
                break;
            }
            else if (i > 0 && num == nums[i - 1])
            {
                continue;
            }

            left = i + 1;
            right = n - 1;

            while (left < right)
            {
                while (left < right && (left > i + 1) && (nums[left - 1] == nums[left]))
                {
                    left++;
                }
                while (left < right && (right < n - 1) && (nums[right + 1] == nums[right]))
                {
                    right--;
                }
                sum = num + nums[left] + nums[right];
                if (left < right && sum == 0)
                {
                    results.push_back({num, nums[left], nums[right]});
                    left++;
                    right--;
                }
                else if (sum < 0)
                {
                    left++;
                }
                else if (sum > 0)
                {
                    right--;
                }
            }
        }

        return results;
    }
};

int main()
{
    std::vector<std::vector<int>> test_cases = {
        {-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6},
        {-1, 0, 1, 2, -1, -4},
    };

    for (auto &nums : test_cases)
    {
        for (auto &vec : Solution().threeSum(nums))
        {
            print_vector(vec);
        }
        std::cout << std::endl;
    }
    return 0;
}
