class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mon = 0
        for x in range(len(prices)):
            if x == len(prices):
                pass
            else:
                j = x+1
                while j<len(prices):
                    mon = max(mon, (prices[j]-prices[x]))
                    j+=1

        return mon