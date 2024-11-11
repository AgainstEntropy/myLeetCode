#include "common.h"

class Solution
{
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        int len = nums.size();
        std::vector<int> idxs = {0, 1};
        while (true) {
            for(idxs[1] = idxs[0]+1; idxs[1] < len; idxs[1]++) {
                if (nums[idxs[0]] + nums[idxs[1]] == target)
                {
                    break;
                }
            }
            if (idxs[1] == len) {
                idxs[0]++;
            } else if (nums[idxs[0]] + nums[idxs[1]] == target) {
                break;
            }
        }

        return idxs;
    }
};

int main() {
    std::vector<int> nums = {11, 2, 7, 15, -1};

    Solution sol;
    std::vector<int> idxs = sol.twoSum(nums, 1);

    std::cout << idxs[0] << "," << idxs[1];

    return 0;
}