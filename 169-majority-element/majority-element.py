class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_freq={}
        for num in nums:
            if num in num_freq:
                num_freq[num]+=1
            else:
                num_freq[num]=1
        max_freq=0
        max_num=None
        for i in num_freq:
            if num_freq[i]>max_freq:
                max_num=i
                max_freq=num_freq[i]
        return max_num