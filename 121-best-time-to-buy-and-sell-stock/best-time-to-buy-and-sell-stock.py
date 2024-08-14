class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minim=prices[0]
        max_profit=0

        for i in prices[1:]:
            if i<minim:
                minim=i
            else:
                max_profit = max(max_profit, i-minim)

        return max_profit