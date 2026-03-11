class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for string in strs:
            char_count = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
            for character in string:
                char_count[character]+=1
            char_count_str = ''.join([ k+str(v) for k, v in char_count.items() ])
            if char_count_str in anagram_map:
                anagram_map[char_count_str].append(string)
            else:
                anagram_map[char_count_str]=[string]
        return list(anagram_map.values())