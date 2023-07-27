from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation)).lower()
        s=''.join(s.split())
        if s==s[::-1]:
            return True
        else:
            return False