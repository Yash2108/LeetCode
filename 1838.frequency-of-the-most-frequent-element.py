#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from statistics import mode

class Solution:

    def method2(self, nums, k):
        
        counts=[]

        for start_point in range(1, len(nums)-1):
            count=1
            temp_k=0+k
            temp_nums=[]+nums

            for idx_to_compare_with in range(start_point, len(temp_nums)):

                diff = [ temp_nums[idx_to_compare_with] - num  for num in temp_nums[:idx_to_compare_with] ]

                print(f"idx_to_compare_with: {idx_to_compare_with}, \
                        diff: {diff}, nums: {temp_nums}, count: {count}")
                
                for idx, val in list(enumerate(diff))[::-1]:
                    
                    if temp_k==0:
                        break

                    if val<=temp_k:                    
                        print(f"val: {val}, k: {k}, count: {count}")
                        print(f"nums before change: {temp_nums}")

                        count+=1
                        temp_k-=val
                        temp_nums[idx]+=val

                        print(f"nums after change: {temp_nums}")
                        print(f"count after change: {count}")
                    else:
                        break

                if temp_k==0:
                    break
            freq={}
            for num in temp_nums:
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1
            
            counts.append(max(freq.values()))
        print(f"Final counts: {counts}")
        return max(counts)

    
    def maxFrequency(self, nums: List[int], k: int) -> int:
        val2 = self.method2(nums, k)
        return val2
# @lc code=end

