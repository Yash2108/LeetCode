class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        for idx in range(len(nums)-2):
            left = idx+1
            right = len(nums)-1

            while left < right:
                current_sum = nums[idx] + nums[left] + nums[right]
                if current_sum == 0:
                    triplets.add((nums[idx], nums[left], nums[right]))
                    left+=1
                elif current_sum<0:
                    left+=1
                else:
                    right-=1
        triplets = [ [ num for num in triplet ] for triplet in triplets ]
        return triplets