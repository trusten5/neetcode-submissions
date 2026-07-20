class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0

        for p in prices:
            profit=max(p-buy, profit)
            buy = min(buy, p)

        return profit
