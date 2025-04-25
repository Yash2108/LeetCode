class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        check which has smaller val
        move that to the right
        add water level with this formula, max(the moved pointers val-height, 0)
        update val of pointer
        '''
        left_idx, right_idx = 0, len(height)-1
        left = height[left_idx]
        right = height[right_idx]
        
        water = 0

        while left_idx < right_idx:
            if left < right:
                left_idx+=1
                water += max( left-height[left_idx], 0 )
                left = max(left, height[left_idx])
            else:
                right_idx-=1
                water += max( right-height[right_idx], 0 )
                right = max(right, height[right_idx])
        return water