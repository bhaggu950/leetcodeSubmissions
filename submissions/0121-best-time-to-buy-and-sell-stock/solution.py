class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxi = 0
        mini = float('inf')
        n = len(prices)
        for i in range(n):
            if mini>prices[i]:
                mini = prices[i]
            else:
                maxi = max(maxi, prices[i]-mini)
        
        return maxi
        
        
