# 每个查询的最漂亮物品
# Most Beautiful Item for Each Query


class Solution:
    def mostBeautifulItem(
        self, items: list[list[int]], queries: list[int]
    ) -> list[int]:
        max_price = max(queries)
        price_to_beauty = dict()
        for p, b in items:
            if p > max_price:
                continue
            price_to_beauty[p] = max(b, price_to_beauty.get(p, 0))

        pb_pairs = sorted(price_to_beauty.items(), key=lambda x: x[0])
        for i in range(1, len(pb_pairs)):
            if pb_pairs[i][1] < pb_pairs[i-1][1]:
                pb_pairs[i] = (pb_pairs[i][0], pb_pairs[i-1][1])

        ans = []
        for q in queries:
            max_beauty = 0
            if pb_pairs:
                if pb_pairs[-1][0] <= q:
                    max_beauty = pb_pairs[-1][1]
                elif pb_pairs[0][0] > q:
                    pass
                else:
                    max_beauty = self.binary_search(pb_pairs, q)
            ans.append(max_beauty)

        return ans

    def binary_search(self, pb_pairs: list[tuple[int, int]], query: int) -> int:
        n = len(pb_pairs)
        left, right = 0, n
        mid = left + (right - left) // 2
        while mid > left:
            if pb_pairs[mid][0] <= query:
                left = mid
            else:
                right = mid
            mid = left + (right - left) // 2

        return pb_pairs[left][1]


if __name__ == "__main__":
    test_cases = [
        ([[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]],[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]),
        ([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [1, 2], [1, 3], [1, 4]], [1]),
        ([[10, 1000]], [5]),
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.mostBeautifulItem(*case))
