class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chara_count=[0 for _ in range(26)]
        for chara in s1:
            chara_count[ord(chara)-ord('a')]+=1
        
        for i in range(len(s2)-len(s1)+1):
            temp=[0 for _ in range(26)]
            for chara in s2[i:i+len(s1)]:
                temp[ord(chara)-ord('a')]+=1
            if temp==chara_count:
                return True
        return False