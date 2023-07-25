#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x>2147483647 or x< -2147483648:
            return 0
        
        if '-' in str(x):
            x='-'+''.join([i for i in reversed(str(x)[1:])])
        else:
            x=''.join([i for i in reversed(str(x))])
        
        x=int(x)
        
        if x>2147483647 or x< -2147483648:
            return 0
        
        return x
# @lc code=end

