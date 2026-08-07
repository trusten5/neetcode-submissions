class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit=0

        for n in prices:
            profit = max(profit, n-buy)
            buy=min(buy, n)

        return profit
