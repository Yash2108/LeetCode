from heapq import heapify, heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        heapify(heap)

        for x, y in points:
            dist=(x**2+y**2)**0.5
            if len(heap)<k:
                heappush(heap, [-dist, x, y])
            else:
                if dist<-heap[0][0]:
                    heappop(heap)
                    heappush(heap, [-dist, x, y])
        return [[i[1], i[2]] for i in heap]