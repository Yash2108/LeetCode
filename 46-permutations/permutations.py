class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def backtrack(perm, pool):
            if not pool:
                result.append(perm)
                return
            
            for idx in range(len(pool)):
                backtrack(perm+[pool[idx]], pool[:idx]+pool[idx+1:])
        
        backtrack([], nums)

        return result