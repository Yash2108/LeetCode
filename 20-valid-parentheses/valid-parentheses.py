class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_brackets=['{', '[', '(']
        mapping={
            ']':'[',
            ')':'(',
            '}':'{'
        }
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                if mapping[bracket]==stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
                