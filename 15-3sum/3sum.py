class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=set()
        nums=sorted(nums)

        for idx_num1 in range(len(nums)-2):
            left = idx_num1+1
            right = len(nums)-1
            while left<right :
                if nums[idx_num1]+nums[left]+nums[right]==0:
                    triplets.add((nums[idx_num1],nums[left],nums[right]))
                    right-=1
                elif nums[idx_num1]+nums[left]+nums[right]<0:
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                else:
                    right-=1
        
        return list([list(i) for i in triplets])