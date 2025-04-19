from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:

        freq=Counter(s)
        freq=[[-cnt, chara]for chara, cnt in freq.items()]
        heapify(freq)

        popped=None
        result=''
        while freq or popped:
            if popped and not freq:
                return ''
            cnt, chara=heappop(freq)
            result+=chara
            cnt+=1

            if popped:
                heappush(freq, popped)
                popped=None
            if cnt!=0:
                popped=[cnt, chara]
        
        return result