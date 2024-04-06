class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start_point=0
        count=defaultdict(lambda: 0)
        longest_len = 0
        for i in range(len(s)):
            count[s[i]]+=1
            while len(s[start_point:i+1])-max(count.items(), key = lambda x:x[1])[1] > k:
                count[s[start_point]]-=1
                start_point+=1
            longest_len = max(longest_len, i-start_point+1)

        return longest_len