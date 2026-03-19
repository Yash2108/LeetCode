class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}

        for idx, num in enumerate(numbers):
            if target - num in mapping:
                return mapping[target - num], idx+1 
            mapping[num] = idx+1
        