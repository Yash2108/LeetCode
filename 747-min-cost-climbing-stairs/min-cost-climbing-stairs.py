class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)-1
        step_1, step_2 = cost[n], cost[n-1]
        step=n-2
        while step>=0:
            step_new = min(step_1, step_2)+cost[step]
            step_1, step_2 = step_2, step_new
            step-=1
        return step_1 if step_1<step_2 else step_2

