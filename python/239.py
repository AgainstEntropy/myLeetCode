# Sliding Window Maximum
# 滑动窗口最大值


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        answer = []
        heap = [(-num, i) for i, num in enumerate(nums[:k])]
        import heapq
        heapq.heapify(heap)
        answer.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            answer.append(-heap[0][0])
        return answer

if __name__ == '__main__':
    test_cases = [
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1], 1),
        ([1,-1], 1),
        ([9,11], 2),
        ([4,-2], 2),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.maxSlidingWindow(*case)
        print(case, '\n', res)