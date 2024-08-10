class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        for idx, num in enumerate(nums):
            if target-num in mapping:
                return [idx, mapping[target-num]]
            mapping[num]=idx