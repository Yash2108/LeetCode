class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''

        brute force:
        have a dictionary where key is number and value is longest length
        start at end
        to the dict add num and len
        go back one space and check for longest len key in dict
        repeat till we reach start
        '''

        num_to_len = {}
        for start in range(len(nums)-1, -1, -1):
            num=nums[start]

            next_options=[]
            
            for nxt in range(start+1, len(nums)):
                if nums[nxt]>num:
                    next_options.append(num_to_len[nums[nxt]])

            if next_options:
                num_to_len[num]=1+max(next_options)
            else:
                num_to_len[num]=1

        return max(num_to_len.values())