class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1

        while start<=end:
            middle = start + (end-start)//2
            print(start, middle, end, nums[middle])
            if nums[middle]==target:
                return middle
            else:
                if target<nums[middle]:
                    end=middle-1
                else:
                    start=middle+1
        return -1