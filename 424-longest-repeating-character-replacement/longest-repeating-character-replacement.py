class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        replacements = 0
        current_idx = 0
        next_idx = 0
        longest=0
        current_len=0
        charCount={}
        while next_idx<len(s):
            if s[next_idx] in charCount:
                charCount[s[next_idx]]+=1
            else:
                charCount[s[next_idx]]=1
            
            freq_char = sorted(charCount.items(), key = lambda x:x[1])[-1]
            replacements_reqd = next_idx-current_idx+1 - freq_char[1]

            while replacements_reqd>k:
                charCount[s[current_idx]]-=1
                freq_char = sorted(charCount.items(), key = lambda x:x[1])[-1]
                replacements_reqd = next_idx-current_idx - freq_char[1]
                current_idx+=1
                    
            current_len=next_idx-current_idx+1
            longest=max(longest, current_len)
            next_idx+=1
        return longest
