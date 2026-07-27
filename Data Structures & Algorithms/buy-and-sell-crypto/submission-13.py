class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        prof = 0

        for p in prices:
            prof = max(prof, p-buy)
            buy = min(p, buy)

        return prof