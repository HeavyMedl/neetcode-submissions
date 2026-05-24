class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        minPrice = None
        for price in prices:
            if minPrice is None or price == min(minPrice, price):
                minPrice = price
            bestProfit = max(bestProfit, price - minPrice)

        return bestProfit