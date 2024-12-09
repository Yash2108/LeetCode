from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles=0
        heap=[]
        heapify(heap)
        counter = Counter(tasks)
        
        for task in counter:
            heappush(heap, [-counter[task], task])
        
        while heap:
            task_completed=[]
            for _ in range(n+1):
                # print(cycles, heap, task_completed)
                if not heap:
                    if not task_completed:
                        break
                    cycles+=1
                    continue
                cycles+=1
                

                task = heappop(heap)
                if task[0]==-1:
                    continue
                task_completed.append([task[0]+1, task[1]])
            for t in task_completed:
                heappush(heap, t)
        return cycles