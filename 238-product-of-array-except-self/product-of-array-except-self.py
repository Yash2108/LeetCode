class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1 for _ in range(len(nums))]
        res=[1 for i in range(len(nums))]
        postfix=1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix*prefix[i]
            postfix*=nums[i]
            
        return res