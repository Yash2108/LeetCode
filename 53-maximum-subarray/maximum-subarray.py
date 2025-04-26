class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=max(nums)
        current=0

        for num in nums:
            current=max(num, current+num)
            res = max(current, res)
        return res