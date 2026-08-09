class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        max_rows, max_cols = m -1, n-1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
        
        for r in range(m):
            for c in range(n):
                if 0 <= r - 1 < m and 0 <= c -1 < n:
                    # print(r,c)
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]


