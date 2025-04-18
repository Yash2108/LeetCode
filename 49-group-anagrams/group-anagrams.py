class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            word_map = [0 for _ in range(26)]
            for chara in word:
                word_map[ord(chara)-ord('a')]+=1
            word_map=''.join([chr(w+ord('a'))+str(c) for w, c in enumerate(word_map)])
            if word_map in anagram_map:
                anagram_map[word_map].append(word)
            else:
                anagram_map[word_map]=[word]
        return [ anagrams for anagrams in anagram_map.values()]
