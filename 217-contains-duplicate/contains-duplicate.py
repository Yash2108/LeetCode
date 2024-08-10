class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping={}
        for num in nums:
            if num in mapping:
                return True
            mapping[num]=num
        return False