class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for idx, num in enumerate(nums):
            if target-num in idx_map:
                return idx_map[target-num], idx
            else:
                idx_map[num]=idx
                