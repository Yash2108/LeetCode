class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        start_point=0
        temp_str=''

        for i in range(len(s)):
            if s[i] not in s[start_point:i]:
                temp_str+=s[i]
                longest=max(longest, len(temp_str))
            else:
                start_point=start_point+s[start_point:i].index(s[i])+1
                temp_str=s[start_point:i+1]
                
        return longest