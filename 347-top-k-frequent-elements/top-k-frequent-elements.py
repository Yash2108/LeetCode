class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for _ in range(len(nums))]
        num_freq={}
        for num in nums:
            if num in num_freq:
                num_freq[num]+=1
            else:
                num_freq[num]=1
        for num in num_freq:
            buckets[num_freq[num]-1].append(num)
        result=[]
        for bucket in buckets[::-1]:
            for num in bucket:
                if len(result)==k:
                    return result
                result.append(num)
        return result