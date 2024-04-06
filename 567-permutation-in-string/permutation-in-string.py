class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=len(s1)
        # s1=sorted(s1)
        s1_count = [0]*26
        for i in s1:
            s1_count[ord(i)-ord('a')]+=1
        s1_count = ''.join([ chr(idx+ord('a'))+str(count) for idx, count in enumerate(s1_count)])
        
        for i in range(len(s2)-window_size+1):
            s2_count = [0]*26
            for character in s2[i:i+window_size]:
                s2_count[ord(character)-ord('a')]+=1
            s2_count = ''.join([ chr(idx+ord('a'))+str(count) for idx, count in enumerate(s2_count)])

            # window=sorted(s2[i:i+window_size])
            if  s2_count == s1_count:
                return True
        return False