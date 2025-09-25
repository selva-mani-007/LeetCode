class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        max_p = 0

        for price in prices:
            mini = min(mini,price)
            profit = price - mini
            max_p = max(max_p,profit)
        return max_p
'''
       l,r=0,1
       maxp=0
       while r<len(prices):
            if prices[l] < prices[r]:
                diff=prices[r] - prices[l]
                maxp=max(diff,maxp)

            else:
                l=r
            r+=1
       return maxp
'''




