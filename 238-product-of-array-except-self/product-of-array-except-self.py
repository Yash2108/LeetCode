class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        for i in range(len(nums)):
            if i==0: 
                prefix[i]=nums[i]
                postfix[len(nums)-i-1] = nums[len(nums)-i-1]
            
            else: 
                prefix[i]=prefix[i-1]*nums[i]
                postfix[len(nums)-i-1] = nums[len(nums)-i-1]*postfix[len(nums)-i]
                
        for i in range(len(nums)):
            if i==0:
                output[i] = postfix[i+1]
            elif i==len(nums)-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1]*postfix[i+1]

        print(prefix)
        print(postfix)
        return output