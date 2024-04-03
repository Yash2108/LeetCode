class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        triplets=[]

        for i, num in enumerate(nums):
            start_point=i+1
            end_point=len(nums)-1
            while end_point>start_point:
                if nums[start_point]+nums[end_point]==-num:
                    triplets.append((num, nums[start_point], nums[end_point]))
                    end_point-=1
                elif nums[start_point]+nums[end_point]<-num:
                    start_point+=1
                else:
                    end_point-=1
        return set(triplets)