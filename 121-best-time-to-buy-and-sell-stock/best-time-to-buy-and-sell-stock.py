class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum = prices[0]
        max_profit=0

        for price in prices[1:]:
            if price<minimum:
                minimum=price
            else:
                max_profit=max(price-minimum, max_profit)
        return max_profit
