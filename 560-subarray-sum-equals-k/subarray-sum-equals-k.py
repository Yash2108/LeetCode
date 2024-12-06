class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output=0
        prefix={0:1}
        current_sum=0
        for i in nums:
            current_sum+=i
            if current_sum-k in prefix:
                output+=prefix[current_sum-k]
            if current_sum in prefix:
                prefix[current_sum]+=1
            else:
                prefix[current_sum]=1
        return output
                