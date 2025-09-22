class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for i in range(n)]

        for t in range(amount+1):
            if t % coins[0] == 0:
                dp[0][t] = 1
        
        for i in range(1,n):
            for t in range(amount+1):
                not_take = dp[i-1][t]
                take = 0
                if coins[i] <= t:
                    take = dp[i][t-coins[i]]
                dp[i][t] = take + not_take
        
        return dp[n-1][amount]
