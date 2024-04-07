class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations=[]

        def backtrack(num_open = 0, num_close = 0, stack=""):
            if num_open == num_close == n:
                combinations.append(stack)
                return
            
            if num_open < n:
                backtrack(num_open+1, num_close, stack+"(")
            
            if num_close < num_open:
                backtrack(num_open, num_close+1, stack+")")
        
        backtrack()

        return combinations