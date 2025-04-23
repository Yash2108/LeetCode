class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        each position can have either open or close brackets
        close brackets are only valid if open>close
        total len of each string=2n
        '''

        result=[]

        def backtrack(paranthesis, open, close):
            if len(paranthesis)==2*n:
                if open==close:
                    result.append(paranthesis)
                return
            backtrack(paranthesis+'(', open+1, close)
            if open>close:
                backtrack(paranthesis+')', open, close+1)
            return
        backtrack('', 0, 0)
        return result