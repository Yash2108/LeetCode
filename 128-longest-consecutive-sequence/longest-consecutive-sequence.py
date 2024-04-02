class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        num_set=set(nums)
        for num in nums:
            if num-1 not in num_set:
                # make a seq starting with this
                length=1
                while num+length in num_set:
                    # add next_num to seq
                    length+=1
                max_len=max(max_len, length)

        return max_len