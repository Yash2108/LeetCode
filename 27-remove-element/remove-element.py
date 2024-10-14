class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer=0
        for idx in range(len(nums)):
            if nums[idx]!=val:
                nums[pointer]=nums[idx]
                pointer+=1
        return pointer