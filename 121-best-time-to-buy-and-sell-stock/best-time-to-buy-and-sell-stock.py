class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minimum=prices[0]

        for val in prices[1:]:
            if val<minimum:
                minimum=val
            profit=max(profit, val-minimum)

        return profit
            