class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        i = 0
        j = 1

        while i<len(prices)-1:
            profit = max(profit, prices[j]-prices[i])
            j+=1
            if j==len(prices):
                i+=1
                j=i+1
        
        return profit