from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles=0
        heap=[]
        heapify(heap)
        counter={}

        for task in tasks:
            if task in counter:
                counter[task]+=1
            else:
                counter[task]=1
        
        for task in counter:
            heappush(heap, [-counter[task], task])
        
        while heap:
            # print("Cycles: ", cycles)
            task_completed=set()
            for _ in range(n+1):
                if not heap:
                    break
                
                task = heappop(heap)
                skip=[]
                while task[1] in task_completed:
                    skip.append(task)
                    if not heap:
                        task=None
                        break
                    task = heappop(heap)
                    # print("Choosing again:", task)
                # print("Task chosen:", task)
                for skipped in skip:
                    heappush(heap, skipped)
                cycles+=1
                
                # print(task, task_completed, cycles)
                if not task:
                    continue                
                task_completed.add(task[1])
                if task[0]==-1:
                    continue
                heappush(heap, [task[0]+1, task[1]])
        return cycles