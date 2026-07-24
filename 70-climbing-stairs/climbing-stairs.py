class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n+1)
        
        """
        0 -> 0
        1 -> 1  dp[1] = 1
        2 -> 1+1, 2     dp[2] = dp[1] + 1
        3 -> 1+1+1, 1+2, 2+1    dp[3] = dp[2] + 1
        4 -> 1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2      dp[4] = dp[3] (-1) + dp[2] (-2)
        """
        if n <= 2:
            return n
        dp[1], dp[2] = 1, 2
        
        for i in range(3,len(dp)):

            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]



