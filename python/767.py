# 重构字符串
# Reorganize String


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = dict()
        for c in s:
            count[c] = count.get(c, 0) + 1

        import heapq

        heap = []
        for c, t in count.items():
            heapq.heappush(heap, [-t, c])

        res = "0"
        while len(heap) >= 2:
            top1 = heapq.heappop(heap)
            top2 = heapq.heappop(heap)
            res += top1[1]
            top1[0] += 1
            res += top2[1]
            top2[0] += 1

            if top1[0] != 0:
                heapq.heappush(heap, top1)
            if top2[0] != 0:
                heapq.heappush(heap, top2)

        if len(heap) == 1:
            if heap[0][0] < -1 or heap[0][1] == res[-1]:
                return ""

            res += heap[0][1]

        return res[1:]


if __name__ == "__main__":
    test_cases = [
        "a",
        "bbbbbbb",
        "aabbcc",
        "ogccckcwmbmxtsbmozli",
        "abbabbaaab",
        "baaba",
        "vvvlo",
        "aab",
        "aaab",
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.reorganizeString(case))
