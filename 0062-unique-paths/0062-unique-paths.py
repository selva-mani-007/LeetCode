class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 :
                    dp[0][0] = 1
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    down = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + down
        
        return dp[m-1][n-1]

"""
        dp = [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
"""
        