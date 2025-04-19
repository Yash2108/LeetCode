class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        longest variable
        two pointers
        one pointer indicates start of substring
        other pointer keeps going forward till a repeat occurs
        for checking repeats, we can use a set so the check is O(1)
        '''

        longest=0
        start=end=0
        hashmap={}
        while end!=len(s): 
            while s[end] in hashmap:  
                del hashmap[s[start]] 
                start+=1 
                longest=max(longest, len(hashmap)) 
            hashmap[s[end]]=end 
            longest=max(longest, len(hashmap))
            end+=1 
        return longest