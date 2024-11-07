# 接雨水
# Trapping Rain Water

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)
                if stack:
                    left = stack[-1] + 1
                    right = i - 1
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ans += high * (right - left + 1)
                else:
                    break
            stack.append(i)
        return ans


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 0, 3, 2, 5], 9),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 9, 4, 5, 3, 2], 1),
        ([5, 4, 1, 2], 1),
    ]

    for height, expected in test_cases:
        ans = Solution().trap(height)
        print(f"trap({height}) = {ans}, answer is {ans == expected}")
