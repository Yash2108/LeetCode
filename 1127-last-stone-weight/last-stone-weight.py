from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapify(stones)
        while len(stones)>1:
            stone1 = -heappop(stones)
            stone2 = -heappop(stones)
            if stone1==stone2:
                continue
            elif stone1>stone2:
                heappush(stones, -(stone1-stone2))
            else:
                heappush(stones, stone1-stone2)
        if stones:
            return -stones[0]
        else:
            return 0