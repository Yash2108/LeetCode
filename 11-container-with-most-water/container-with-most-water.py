class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_pointer = 0
        end_pointer=len(height)-1
        area=0
        while start_pointer<end_pointer:
            new_area= min(height[start_pointer], height[end_pointer]) * (end_pointer-start_pointer)

            if new_area>area:
                area=new_area
            
            if height[start_pointer]>height[end_pointer]:
                end_pointer-=1
            else:
                start_pointer+=1
        return area