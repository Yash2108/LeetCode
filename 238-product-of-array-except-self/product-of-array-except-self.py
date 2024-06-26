class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        for i in range(len(nums)-1):
            output[i+1]=nums[i]*output[i]

        post=1
        for i in range(len(nums)-1, -1, -1):
            output[i]*=post
            post*=nums[i]

        return output