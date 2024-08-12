class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(i for i in s if i in 'abcdefghijklmonpqrstuvwxyz0123456789')

        left, right = 0, len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True