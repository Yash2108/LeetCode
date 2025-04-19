class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=''
        toggle = True
        while word1 and word2:
            if toggle:
                result+=word1[0]
                word1=word1[1:]
            else:
                result+=word2[0]
                word2=word2[1:]
            toggle=not toggle
        if word1:
            result+=word1
        else:
            result+=word2
        return result