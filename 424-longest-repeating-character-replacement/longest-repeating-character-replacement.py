class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        current_idx = 0
        next_idx = 0
        longest=0
        current_len=0
        charCount={}


        for next_idx in range(len(s)):
            if s[next_idx] in charCount:
                charCount[s[next_idx]]+=1
            else:
                charCount[s[next_idx]]=1
            
            freq_char = max(charCount.values())
            replacements_reqd = next_idx-current_idx+1 - freq_char

            while replacements_reqd>k:
                charCount[s[current_idx]]-=1
                current_idx+=1
                freq_char = max(charCount.values())
                replacements_reqd = next_idx-current_idx+1 - freq_char
                    
            current_len=next_idx-current_idx+1
            longest=max(longest, current_len)
        return longest
