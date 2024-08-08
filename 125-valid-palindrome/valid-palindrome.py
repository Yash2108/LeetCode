class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets='abcdefghijklmnopqrstuvwxyz0123456789'
        s=s.lower()
        final_str = ''.join([i for i in s if i in alphabets])

        if final_str==final_str[::-1]:
            return True
        else:
            return False