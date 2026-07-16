class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i=0
        buy = max(prices)
        while i < len(prices):
            buy = min(buy, prices[i])
            sell_tdy = prices[i]-buy
            profit=max(profit, sell_tdy)
            i+=1
        
        return profit