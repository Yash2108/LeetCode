from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join([i for i in s if i not in punctuation and i!=' ']).lower()
        if s[::-1]==s:
            return True
        return False