class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        s=''.join([i for i in s if i.isalnum()]).lower()
        for i in range(len(s)//2):
            if s[i]!=s[-i-1]:
                return False
        return True