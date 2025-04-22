class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=dict()
        longest=0
        start, end = 0, 0

        while end!=len(s):
            while s[end] in substring:
                del substring[s[start]]
                start+=1
            substring[s[end]]=end
            longest = max(longest, len(substring))
            end+=1
        return longest