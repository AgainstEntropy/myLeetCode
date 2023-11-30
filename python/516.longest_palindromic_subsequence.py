class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        m = [[0] * (n) for _ in range(n)]

        for i in range(n):
            m[i][i] = 1

        for i in range(1, n):
            for j in range(n-i):
                if s[j] == s[j+i]:
                    m[j][j+i] = m[j+1][j+i-1] + 2
                else:
                    m[j][j+i] = max(m[j+1][j+i], m[j][j+i-1])
        
        return m[0][n-1]
    

if __name__ == '__main__':
    test_case = [
        "bbbab",
        "cbbd",
    ]

    sol = Solution()
    for case in test_case:
        res = sol.longestPalindromeSubseq(case)
        print(case, '\t', res)