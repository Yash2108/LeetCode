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
            # temp=[]
            diff=len(self.minheap)-self.k
            for _ in range(diff):
                # temp.append(
                heapq.heappop(self.minheap)
                # )
            # self.minheap=temp
            # heapq.heapify(self.minheap)


    def add(self, val: int) -> int:
        # print(self.minheap)
        if self.minheap:
            if len(self.minheap)<self.k:
                heapq.heappush(self.minheap, val)
            elif val>self.minheap[0]:
                heapq.heappush(self.minheap, val)
                heapq.heappop(self.minheap)
        else: 
            heapq.heappush(self.minheap, val)
        return self.minheap[0]
            # return val
    #     self.maxheap=[-i for i in nums]
    #     self.k=k
    #     heapq.heapify(self.maxheap)
    #     self.maintainHeap()
    # def maintainHeap(self):
    #     temp=[]
    #     if len(self.maxheap)>self.k:
    #         for _ in range(self.k):
    #             temp.append(heapq.heappop(self.maxheap))
    #         heapq.heapify(temp)
    #         self.maxheap=temp

    # def add(self, val: int) -> int:
    #     heapq.heappush(self.maxheap, -val)
    #     self.maintainHeap()
    #     temp=self.maxheap.copy()
    #     for _ in range(self.k):
    #         =heapq.heappop(temp)
    #     return -out

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)