class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=set()
        nums=sorted(nums)


        for idx, num in enumerate(nums):

            left, right = idx+1, len(nums)-1
            while left < right:

                if nums[left] + nums[right] + num == 0:
                    triplets.add((nums[left], nums[right], num))
                    # break
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                elif nums[left] + nums[right] + num < 0:
                    left+=1
                else:
                    right-=1
        
        return triplets