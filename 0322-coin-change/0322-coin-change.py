class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [[0]*(amount+1) for i in range(n)]

        for t in range(amount+1):
            if t % coins[0] == 0:
                dp[0][t] = t//coins[0]
            else:
                dp[0][t] = float("inf")

        for i in range(1,n):
            for t in range(amount+1):
                not_take = dp[i-1][t]
                take = float("inf")
                if coins[i] <= t:
                    take = 1 + dp[i][t-coins[i]]
                dp[i][t] = min(take,not_take)
        
        return -1 if dp[n-1][amount] >= float("inf") else dp[n-1][amount]
"""
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a],1+dp[a-coin])
        return dp[amount] if dp[amount] != amount+1 else -1
"""