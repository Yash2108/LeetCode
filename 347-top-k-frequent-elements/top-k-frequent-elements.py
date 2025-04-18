class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq={}
        for num in nums:
            if num in num_freq:
                num_freq[num]+=1
            else:
                num_freq[num]=1
        sorted_freq=sorted(num_freq.items(), key = lambda x:x[1], reverse=True)[:k]
        return [i[0] for i in sorted_freq]