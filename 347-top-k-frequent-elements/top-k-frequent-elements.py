import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict=defaultdict(int)
        for num in nums:
            count_dict[num]+=1
        heap=[(-val, key) for key, val in count_dict.items()]
        heapq.heapify(heap)
        output=[]
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
        return output