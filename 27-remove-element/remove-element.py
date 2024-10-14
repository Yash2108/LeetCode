class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        pointer=0
        for idx in range(len(nums)):
            if nums[idx]!=val:
                k+=1
                nums[pointer]=nums[idx]
                pointer+=1
        return k