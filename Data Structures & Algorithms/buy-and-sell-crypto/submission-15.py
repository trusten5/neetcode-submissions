class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        prof = 0

        for n in prices:
            prof = max(prof, n-buy)
            buy=min(buy, n)
        return prof