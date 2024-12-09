class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        mapping={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        alphabets='abcdefghijklmnopqrstuvwxyz'
        output=''
        removals=[]
        for idx, chara in enumerate(s):
            output+=chara
            if chara in alphabets:
                continue
            if chara not in mapping:
                stack.append([chara, idx])
            else:
                if stack:
                    if stack[-1][0]!=mapping[chara]:
                        removal.append(stack[-1][1])
                        removal.append(idx)
                    stack.pop(-1)
                else:
                    removals.append(idx)

        while stack:
            bracket= stack.pop(-1)
            removals.append(bracket[1])
        final_output=[]
        for idx in range(len(s)):
            if idx not in removals:
                final_output.append(s[idx])
        return ''.join(final_output)