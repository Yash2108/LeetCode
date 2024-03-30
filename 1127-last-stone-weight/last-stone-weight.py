from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapify(stones)
        while len(stones)>1:
            y=-1*heappop(stones)
            x=-1*heappop(stones)
            if x==y:
                continue
            else:
                heappush(stones, -1*(y-x))
        if stones: return -1*stones[0]
        else: return 0