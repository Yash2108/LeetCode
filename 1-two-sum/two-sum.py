class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        for idx, n in enumerate(nums):
            if target-n in mapping:
                return [mapping[target-n], idx]
            mapping[n]=idx
        
        return None