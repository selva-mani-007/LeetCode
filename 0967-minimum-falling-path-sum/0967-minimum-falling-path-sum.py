class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for i in range(n)]

        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(n):
                down = matrix[i][j] + dp[i+1][j]
                left_diag = matrix[i][j] + dp[i+1][j-1] if j > 0 else float("inf")
                right_diag = matrix[i][j] + dp[i+1][j+1] if j < n-1 else float("inf")
                dp[i][j] = min(down,left_diag,right_diag)
        
        return min(dp[0])