from heapq import heappop, heappush, heapify

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapify(heap)

        max_values=[]
        for i in range(len(nums)):
            if len(heap)>=k:
                while (-1*heap[0][0]) > nums[i] and i-heap[0][1]>=k:
                    heappop(heap)
                    if len(heap)==0:
                        break

            heappush(heap, [-1*nums[i], i])
            if len(heap)>=k:
                max_values.append(-1 * heap[0][0])
        return max_values
            