import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict={}
        for word in words:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1
        
        heap = [(-count, word) for word, count in word_dict.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]