class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        r1, r2, ..., r9
        c1, c2, ..., c9
        b1, b2, ..., b9
        '''

        rules={}
        for i in range(9):
            rules['r'+str(i)]=[]
            rules['c'+str(i)]=[]
            rules['b'+str(i//3)+str(i%3)]=[]
        
        for row_idx in range(len(board)):
            for col_idx in range(len(board[row_idx])):
                val=board[row_idx][col_idx]
                if val=='.':
                    continue
                if val in rules['r'+str(row_idx)] or val in rules['c'+str(col_idx)] or val in rules['b'+str(row_idx//3)+str(col_idx//3)]:
                    return False
                else:
                    rules['r'+str(row_idx)].append(val)
                    rules['c'+str(col_idx)].append(val)
                    rules['b'+str(row_idx//3)+str(col_idx//3)].append(val)
        return True