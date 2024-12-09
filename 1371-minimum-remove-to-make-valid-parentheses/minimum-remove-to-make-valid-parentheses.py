class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        alphabets='abcdefghijklmnopqrstuvwxyz'
        removals=[]
        for idx, chara in enumerate(s):
            if chara=='(':
                stack.append([chara, idx])
            elif chara==')':
                if stack:
                    stack.pop(-1)
                else:
                    removals.append(idx)

        while stack:
            removals.append(stack.pop(-1)[1])

        output=[]

        for idx in range(len(s)):
            if idx not in removals:
                output.append(s[idx])
        return ''.join(output)