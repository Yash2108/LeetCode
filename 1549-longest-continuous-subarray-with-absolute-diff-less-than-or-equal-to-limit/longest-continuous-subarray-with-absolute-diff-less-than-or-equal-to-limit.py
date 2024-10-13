from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left=0
        right=0
        longest=0
        sl = SortedList()

        while right < len(nums):
            sl.add(nums[right])
            while sl[-1]-sl[0] > limit:
                sl.remove(nums[left])
                left+=1         
            longest = max(longest, right-left+1)
            right+=1

        return longest
            