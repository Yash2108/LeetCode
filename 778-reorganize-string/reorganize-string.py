from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        '''

        we can take count of all characters.
        have a result string. 
        we always add the most frequent character to the string.
        we cant repeat characters so we keep note of the last used.
        keep adding till we either run out of characters or our only choice is to repeat.

        '''

        freq=Counter(s)
        freq=list(freq.items())
        freq = [[-i[1], i[0]] for i in freq]
        heapify(freq)

        result=''
        last_used=None

        while freq: 
            most_freq=heappop(freq)
            if result and result[-1]==most_freq[1]: 
                return ''

            result+=most_freq[1] 
            most_freq[0]+=1 
            if last_used and last_used[0]<0: 
                heappush(freq, last_used) 
            last_used = most_freq 
        
        if last_used[0]<0:
            return ''

        return result