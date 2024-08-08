import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original=[i for i in nums]
        self.new_nums=[i for i in nums]

    def reset(self) -> List[int]:
        self.new_nums = [i for i in self.original] 
        return self.new_nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.new_nums)
        return self.new_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()