# Merge Intervals
# 合并区间


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(interval[1], res[-1][1])]
            else:
                res.append(interval)
                    
        return res
            

if __name__ == '__main__':
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]],),
        ([[1,4],[4,5]],),
    ]

    sol = Solution()
    for case in test_cases:
        res = sol.merge(*case)
        print(case, '\n', res)