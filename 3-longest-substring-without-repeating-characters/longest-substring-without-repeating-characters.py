class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        start_point=0
        temp_len=0
        temp_str=''
        for i in range(len(s)):
            print(s[i], s[start_point:i])
            print(longest, s[start_point:i], temp_str)
            if s[i] not in s[start_point:i]:
                temp_str+=s[i]
                # temp_len+=1
                longest=max(longest, len(temp_str))
                print('not in')
            else:
                print('is in', start_point, s[start_point:i])
                start_point=start_point+s[start_point:i].index(s[i])+1
                temp_str=s[start_point:i+1]
                print('after', start_point)
                # temp_len=i-start_point

            print()
        return longest