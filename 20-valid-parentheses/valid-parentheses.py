class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            ']':'[',
            ')':'(',
            '}':'{'
        }
        for bracket in s:
            if bracket in mapping.values():
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                elif mapping[bracket]==stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
                