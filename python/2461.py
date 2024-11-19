# Maximum Sum of Distinct Subarrays With Length K

from common import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_dict = dict()
        count = 0

        cur_sum = 0
        for i in range(k):
            num = nums[i]
            if (curr := count_dict.get(num, 0)) == 0:
                count += 1

            count_dict[num] = curr + 1
            cur_sum += num

        max_sum = cur_sum if count == k else 0
        for i in range(k, n):
            if (curr := count_dict.get(nums[i], 0)) == 0:
                count += 1

            count_dict[nums[i]] = curr + 1
            count_dict[nums[i - k]] -= 1
            if count_dict[nums[i - k]] == 0:
                count -= 1

            cur_sum = cur_sum + nums[i] - nums[i - k]

            if count == k:
                max_sum = max(max_sum, cur_sum)

        return max_sum


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2], 2),
        ([1, 5, 4, 2, 9, 9, 9], 3),
        ([4, 4, 4], 3),
    ]

    sol = Solution()

    for nums, k in test_cases:
        print(sol.maximumSubarraySum(nums, k))
