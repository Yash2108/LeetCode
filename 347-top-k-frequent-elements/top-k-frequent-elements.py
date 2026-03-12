from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count={}
        for num in nums:
            if num in num_count:
                num_count[num]+=1
            else:
                num_count[num]=1
        num_count_ls = list(num_count.items())
        num_count_ls = sorted(num_count_ls, key= lambda k:k[1])
        output = [num for num, cnt in num_count_ls]
        return output[-k:]