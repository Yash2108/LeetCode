from itertools import combinations

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count={}
        for num in arr:
            if num in count:
                count[num]+=1
            else:
                count[num]=1

        answer=0

        for idx, num in enumerate(arr):
            count[num]-=1
            for i in range(idx):
                last = target-num-arr[i]
                if target-num-arr[i] in count:
                    answer = (answer+count[last])%(10**9+7)
        return answer            