from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        s=''.join([i for i in s if i not in punctuation and i!=' ']).lower()
        # i=0
        # j=len(s)-1
        for i in range(len(s)//2):
            if s[i]!=s[-i-1]:
                return False
            # i+=1
            # j-=1
        return True