from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq={}
        for num in nums:
            if num in num_freq:
                num_freq[num]+=1
            else:
                num_freq[num]=1
        heapify_ls=[]
        heapify(heapify_ls)
        for num in num_freq:
            heappush(heapify_ls, [num_freq[num], num])
            if len(heapify_ls)>k:
                heappop(heapify_ls)
        return [i[1] for i in heapify_ls[::-1]]