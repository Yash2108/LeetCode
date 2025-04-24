from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        heapify(self.left)
        heapify(self.right)

    def addNum(self, num: int) -> None:

        heappush(self.left, -num)

        if len(self.left)-len(self.right)==2:
            heappush(self.right, -heappop(self.left))

        if self.left and self.right:
            while -self.left[0]>self.right[0]:

                heappush(self.right, -heappop(self.left))
                heappush(self.left, -heappop(self.right))


    def findMedian(self) -> float:

        if len(self.left)>len(self.right):
            return -self.left[0]

        elif len(self.left)<len(self.right):
            return self.right[0]
            
        else:
            return (-self.left[0]+self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()