class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: 
            return 0
        maxProf = 0
        l, r = 0, 1
        minPrice = prices[l]
        # Input: prices = 
        # [10,1,5,6,7,1]
        #   l
        #     r
        # Output: 6
        while r < len(prices):
            maxProf = max(maxProf, prices[r] - prices[l])

            if prices[r] < prices[l]:
                # set l to r?
                l = r
            r += 1


        return maxProf