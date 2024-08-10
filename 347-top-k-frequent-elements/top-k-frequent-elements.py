class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping={}
        for num in nums:
            if num in mapping:
                mapping[num]+=1
            else:
                mapping[num]=1

        sorted_nums = sorted(mapping.items(), key=lambda k: k[1], reverse=True)
        return [num[0] for num in sorted_nums[:k]]