class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit(maxsplit=1)[-1])