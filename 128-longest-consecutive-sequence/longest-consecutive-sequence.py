class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs=[]
        num_set=set(nums)
        for num in nums:
            if num-1 not in num_set:
                # make a seq starting with this
                seq=[num]
                next_num=num+1
                while next_num in num_set:
                    # add next_num to seq
                    seq.append(next_num)
                    next_num+=1
                seqs.append(len(seq))
        if seqs:
            return max(seqs)
            # return max([len(i) for i in seqs])
        else:
            return 0