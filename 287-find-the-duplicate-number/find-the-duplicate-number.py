class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pointer=nums[0]
        jumper=nums[nums[0]]

        while nums[pointer]!=nums[jumper]:
            pointer=nums[pointer]
            jumper=nums[nums[jumper]]

        second_pointer=0

        while nums[pointer]!=nums[second_pointer]:
            pointer=nums[pointer]
            second_pointer=nums[second_pointer]

        return nums[pointer]