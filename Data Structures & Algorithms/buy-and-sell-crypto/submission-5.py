class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i=0
        buy = max(prices)
        for p in prices:
            buy = min(buy, p)
            sell_tdy = p-buy
            profit=max(profit, sell_tdy)
        
        return profit