# Kth Largest Element in an Array
# 数组中的第K个最大元素


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return min_heap[0]
    

if __name__ == '__main__':
    test_cases = [
        ([3,2,1,5,6,4], 2),
        ([3,2,3,1,2,4,5,5,6], 4),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.findKthLargest(*case)
        print(case, '\n', res)