from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left=0
        right=0
        longest=0
        sl = SortedList()
        # min_heap, max_heap = [], []
        # min_num, max_num = nums[left], nums[left]

        while right < len(nums):
            sl.add(nums[right])
            while sl[-1]-sl[0] > limit:
                sl.remove(nums[left])
                left+=1
                
                # if min_num>nums[right]:
                #     min_num=nums[right]

                # elif max_num<nums[right]:
                #     max_num=nums[right]

          
            longest = max(longest, right-left+1)
            right+=1

        # while left!=len(nums):

        #     print(f"left: {left}, right: {right},", end='')

        #     if right==len(nums):
        #         if left==len(nums)-1:
        #             print('break0')
        #             break
        #         left+=1
        #         right=left+1
        #         min_num, max_num = nums[left], nums[left]
        #         print('break1')
        #         continue

        #     if min_num>nums[right]:
        #         min_num=nums[right]

        #     elif max_num<nums[right]:
        #         max_num=nums[right]
        #     else:
        #         right+=1
        #         print('break2')
        #         continue

        #     diff = max_num - min_num
        #     if diff<=limit:
        #         longest=max(longest, right-left+1)
        #     print(f"longest: {longest}, min_num: {min_num}, max_num: {max_num}")
        #     right+=1

        return longest
            