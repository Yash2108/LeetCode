class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        triplets=[]

        for i, num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start_point=i+1
            end_point=len(nums)-1
            while end_point>start_point:
                if nums[start_point]+nums[end_point]==-num:
                    triplets.append((num, nums[start_point], nums[end_point]))
                    start_point+=1
                    while start_point<end_point and nums[start_point-1]==nums[start_point]:
                        start_point+=1
                elif nums[start_point]+nums[end_point]<-num:
                    start_point+=1
                else:
                    end_point-=1
        return triplets