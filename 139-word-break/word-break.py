class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        we go reverse
        maintain a dict
        default val of len(s) to be true
        check for every word, if word matches and its next idx in found_match, mark as true
        default it to false at the end


        leetcode, words=['leet', 'code']
        len(s)=8
        7=False
        6=False
        5=False
        4=True, i=4, word_len=4, s[4:8]
        '''
        found_match={len(s):True}
        
        for i in range(len(s), -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i+word_len>len(s):
                    continue
                if s[i:i+word_len]==word and found_match[i+word_len]==True:
                    found_match[i]=True
            if i not in found_match:
                found_match[i]=False
        return found_match[0]