class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        found_match=defaultdict(list)
        found_match[len(s)]=['']

        for idx in range(len(s), -1, -1):
            for word in wordDict:
                word_len = len(word)

                if idx+word_len>len(s):
                    continue
                
                if s[idx:idx+word_len]==word and len(found_match[idx+word_len])>0:
                    for combination in found_match[idx+word_len]:
                        new_word=s[idx:idx+word_len]+' '+combination
                        found_match[idx].append(new_word.strip())
            if idx not in found_match:
                found_match[idx]=[]
        return found_match[0]