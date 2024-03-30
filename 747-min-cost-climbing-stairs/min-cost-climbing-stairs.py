class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)-1
        dp={n:cost[n], n-1:cost[n-1]}
        step=n-2
        while step>=0:
            dp[step]=min(dp[step+1], dp[step+2])+cost[step]
            step-=1
            # print(dp)
        return dp[0] if dp[0]<dp[1] else dp[1]

