class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for num in nums:
            if num-1 in nums:
                continue
            else:
                temp=1
                while num+1 in nums:
                    temp+=1
                    num+=1
                longest=max(temp, longest)

        return longest