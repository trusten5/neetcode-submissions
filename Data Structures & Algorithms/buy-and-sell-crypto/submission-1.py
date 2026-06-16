class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mon = 0
        min_price = max(prices)

        for x in prices:
            if x < min_price:
                min_price = x
            profit = x - min_price

            mon = max(profit, mon)

        return mon