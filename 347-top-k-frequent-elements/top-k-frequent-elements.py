from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = Counter(nums)
        freq_buckets = [[] for _ in range(len(nums)) ]

        for num, freq in count_freq.items():
            freq_buckets[freq-1].append(num)

        result=[]

        for bucket in freq_buckets[::-1]:
            for num in bucket:
                result.append(num)
                if len(result)==k:
                    return result