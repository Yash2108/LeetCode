class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=0

        for command in logs:
            if command=="../":
                if stack!=0:
                    stack-=1
            elif command=='./':
                continue
            else:
                stack+=1
        return stack