class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        combinations=[]

        def backtrack(num_open = 0, num_close = 0):
            if num_open == num_close == n:
                combinations.append("".join(stack))
                return
            
            if num_open < n:
                stack.append("(")
                backtrack(num_open+1, num_close)
                stack.pop(-1)
            
            if num_close < num_open:
                stack.append(")")
                backtrack(num_open, num_close+1)
                stack.pop(-1)
        
        backtrack()

        return combinations