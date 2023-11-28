# include<iostream>
# include<vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int len = nums.size();
        vector<int> idxs = {0, 1};
        while (true) {
            for(idxs[1] = idxs[0]+1; idxs[1] < len; idxs[1]++) {
                if (nums[idxs[0]] + nums[idxs[1]] == target) { 
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
    vector<int> nums = {11,2,7,15,-1};

    Solution sol;
    vector<int> idxs = sol.twoSum(nums, 1);

    cout << idxs[0] << "," << idxs[1];

    return 0;
}