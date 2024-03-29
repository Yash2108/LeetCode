import heapq

class KthLargest:
    '''
    use max heap
    store numbers in heap
    initialize heap and k in init
    append val in add function
    iterate through k values in heap to get return value in add function
    '''
    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k=k
        heapq.heapify(self.minheap)

        if len(self.minheap)>self.k:
            diff=len(self.minheap)-self.k
            for _ in range(diff):
                heapq.heappop(self.minheap)


    def add(self, val: int) -> int:
        if self.minheap:
            if len(self.minheap)<self.k:
                heapq.heappush(self.minheap, val)
            elif val>self.minheap[0]:
                heapq.heappush(self.minheap, val)
                heapq.heappop(self.minheap)
        else: 
            heapq.heappush(self.minheap, val)
        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)