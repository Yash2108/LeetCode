from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join([i for i in s if i not in punctuation and i!=' ']).lower()
        i=0
        j=len(s)-1
        while i<=j:
            print(i, j)
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True