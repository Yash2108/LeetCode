class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end_point=len(numbers)-1
        start_point=0

        while end_point>start_point:
            if numbers[start_point]+numbers[end_point]==target:
                return [start_point+1, end_point+1]
            elif numbers[start_point]+numbers[end_point]>target:
                end_point-=1
            else:
                start_point+=1

