class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        a_ord=ord('a')
        for word in strs:
            counts=[0 for _ in range(26)]
            for chara in word:
                counts[ord(chara)-a_ord]+=1
            counts=''.join([chr(idx+a_ord)+str(num) for idx, num in enumerate(counts) ])
            anagrams[counts].append(word)
        return list(anagrams.values())