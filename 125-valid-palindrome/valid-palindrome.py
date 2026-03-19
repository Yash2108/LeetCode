class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join([character for character in s if character.isalnum() ]).lower()
        reverse_s = cleaned_s[::-1]

        return cleaned_s == reverse_s