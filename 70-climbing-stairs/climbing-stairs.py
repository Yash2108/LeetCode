class Solution:
    
    def climbStairs(self, n: int) -> int:
        dp={n:1, n-1:1}
        step=n-2
        while step>=0:
            dp[step]=dp[step+1]+dp[step+2]
            step-=1
        return dp[0]