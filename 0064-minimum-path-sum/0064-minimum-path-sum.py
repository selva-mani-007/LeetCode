class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    up = grid[i][j] + dp[i-1][j] if i > 0 else float("inf")
                    left = grid[i][j] + dp[i][j-1] if j > 0 else float("inf")
                    dp[i][j] = min(up,left)
        
        return dp[m-1][n-1]