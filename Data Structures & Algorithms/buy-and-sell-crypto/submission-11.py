class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        prof = 0

        for p in prices:
            prof = max(p-buy, prof)
            buy = min(buy, p)
        
        return prof