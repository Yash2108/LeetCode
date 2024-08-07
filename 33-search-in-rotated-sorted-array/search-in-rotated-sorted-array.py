class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0  
            else:
                return -1
        
        start, end = 0, len(nums)-1
        while start<=end:
            mid = (end + start)//2
            # print(start, end, mid)
            if nums[mid]==target:
                return mid

            elif nums[mid]>nums[end]: # if mid is greater than end
                if target<nums[mid]: # if target is smaller than the middle,
                    if target>=nums[start]: # compare with start. if target is greater than equal to start, search left
                        end=mid-1
                        # print('Case 1')
                    else: # compare with start. if target is smaller than start, search right
                        # print('Case 2')
                        start=mid+1
                else: # if target is greater than the middle, search right side
                    # print('Case 3')
                    start=mid+1
            elif nums[mid]<nums[start]: # if mid is smaller than start
                if target>nums[mid]: # if target is greater than middle
                    if target>=nums[start]: # compare with start. if target is greater than start, search left
                        # print('Case 4')
                        end=mid-1
                    else: # compare with start. if target is smaller than start, search right
                        # print('Case 5')
                        start=mid+1
                else: # if target is smaller than middle, search left
                    # print('Case 6')
                    end=mid-1
            else:
                if target>nums[mid]:
                    # print('Case 7')
                    start = mid+1
                else:
                    # print('Case 8')
                    end=mid-1 
        return -1
