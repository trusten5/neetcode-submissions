class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = float('inf')

        for p in prices:
            prof = max(prof, p-buy)
            buy=min(p, buy)
        
        return prof