class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict=defaultdict(list)
        for string in strs:
            chara_count=[0 for i in range(26)]
            for chara in string:
                chara_count[ord(chara)-97]+=1

            chara_count_str=''.join([ chr(idx+97)+str(count) for idx, count in enumerate(chara_count)])
            
            # if chara_count_str in anagram_dict.keys():
            anagram_dict[chara_count_str].append(string)
            # else:
            #     anagram_dict[chara_count_str]=[string]
        return anagram_dict.values()