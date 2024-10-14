class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_count=[0 for _ in range(26)]
        for chara in s1:
            s1_count[ord(chara)-ord('a')]+=1
        
        s2_count=[0 for _ in range(26)]
        for chara in s2[:len(s1)]:
            s2_count[ord(chara)-ord('a')]+=1

        for i in range(len(s2)-len(s1)):
            if s2_count==s1_count:
                return True
            s2_count[ord(s2[i])-ord('a')]-=1
            s2_count[ord(s2[i+len(s1)])-ord('a')]+=1
        return s2_count==s1_count