class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0 
        right=len(numbers)-1

        while left<right and numbers[left]+numbers[right]!=target:
            if numbers[left]<target-numbers[right]:
                left+=1
            else:
                right-=1
        return [left+1, right+1]