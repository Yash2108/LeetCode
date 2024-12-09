from heapq import heapify, heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=[]
        self.k = k
        heapify(self.nums)
        for num in nums:
            if len(self.nums)==self.k:
                heappush(self.nums, num)
                heappop(self.nums)
            else:
                heappush(self.nums, num)      

    def add(self, val: int) -> int:
        if len(self.nums)==self.k:
            heappush(self.nums, val)
            heappop(self.nums)
        else:
            heappush(self.nums, val)      
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)