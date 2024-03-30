class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict={}
        for string in strs:
            chara_count={}
            for chara in string:
                if chara in chara_count:
                    chara_count[chara]+=1
                else:
                    chara_count[chara]=1
            chara_count_str=''.join([str(key)+str(val) for key, val in sorted(chara_count.items(), key=lambda k: k[0])])
            
            if chara_count_str in anagram_dict.keys():
                anagram_dict[chara_count_str].append(string)
            else:
                anagram_dict[chara_count_str]=[string]
        return anagram_dict.values()