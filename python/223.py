# Rectangle Area
# 矩形面积


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        def area(x1: int, y1: int, x2: int, y2: int) -> int:
            w = x2 - x1
            h = y2 - y1
            return w * h if (w > 0 and h > 0) else 0

        ix1 = max(ax1, bx1)
        iy1 = max(ay1, by1)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)

        area_a = area(ax1, ay1, ax2, ay2)
        area_b = area(bx1, by1, bx2, by2)
        area_i = area(ix1, iy1, ix2, iy2)

        return area_a + area_b - area_i


if __name__ == "__main__":
    test_cases = [
        (-3, 0, 3, 4, 0, -1, 9, 2),
        (-2, -2, 2, 2, -2, -2, 2, 2),
        (-2, -2, 2, 2, 3, 3, 4, 4)
    ]

    sol = Solution()
    for case in test_cases:
        print(sol.computeArea(*case))
