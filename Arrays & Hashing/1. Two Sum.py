class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx1=0
        while idx1<len(nums)-1:
            for idx2 in range(idx1+1, len(nums)):
                if nums[idx1]  + nums[idx2] == target:
                    return [idx1, idx2]
            idx1+=1