class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={0:0}
        coins=sorted(coins)
        for i in range(amount+1):
            possibilities=[]
            for coin in coins:
                if i<coin:
                    break
                if i-coin not in dp:
                    continue
                possibilities.append(1+dp[i-coin])
            if possibilities:
                dp[i]=min(possibilities)
        if amount in dp:
            return dp[amount]
        return -1
