class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        go one by one
        check if nums[idx+1]>nums[idx+2]+nums[idx]
            then skip this and take next
        increment extra after operation
        '''

        loot={}
        
        for idx in range(len(nums)-1, -1, -1): # idx=0 l {3:2, 2:1, 1:3}
            if idx==len(nums)-1: # idx=0 l {3:2, 2:1, 1:3}
                loot[idx]=nums[idx] # idx=2 l {3:2, 2:1}
                continue        
            if idx==len(nums)-2: # idx=0 l {3:2, 2:1, 1:3}
                loot[idx]=max(nums[idx], nums[idx+1]) # idx=2 l {3:2, 2:1}
                continue                
            loot[idx]=max(loot[idx+1], nums[idx]+loot[idx+2]) # idx=0 l {3:2, 2:1, 1:3}
        return max(loot.values())