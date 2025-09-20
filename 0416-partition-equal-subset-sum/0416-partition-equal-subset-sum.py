class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        dp = [[False]*(target+1) for i in range(n)]

        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1,n):
            for t in range(1,target+1):
                not_pick = dp[i-1][t]
                pick = False
                if target >= nums[i]:
                    pick = dp[i-1][t-nums[i]]
                dp[i][t] = pick or not_pick
        
        return dp[n-1][target]