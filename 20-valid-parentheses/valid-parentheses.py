class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for bracket in s:
            if bracket in mapping and stack and stack[-1]==mapping[bracket]:
                stack.pop(-1)
            else:
                stack.append(bracket)
        if stack:
            return False
        else:
            return True