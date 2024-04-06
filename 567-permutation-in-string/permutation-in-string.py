class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=len(s1)
        s1=sorted(s1)
        for i in range(len(s2)-window_size+1):
            window=sorted(s2[i:i+window_size])
            if  window== s1:
                return True
        return False