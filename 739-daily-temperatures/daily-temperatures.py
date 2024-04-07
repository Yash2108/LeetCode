class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]

        for idx, val in enumerate(temperatures):
            while stack and val>stack[-1][1]:
                temp=stack.pop(-1)
                output[temp[0]] = idx-temp[0]
            stack.append([idx, val])

        return output

        