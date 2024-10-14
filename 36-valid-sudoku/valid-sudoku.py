class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rules={}
        for i in range(9):
            rules['r'+str(i)]=[]
            rules['c'+str(i)]=[]
        for i in range(3):
            for j in range(3):
                rules['b'+str(i)+str(j)]=[]

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in rules['r'+str(i)] or\
                    board[i][j] in rules['c'+str(j)] or \
                    board[i][j] in rules['b'+str(i//3)+str(j//3)]:
                    return False
                else:
                    rules['r'+str(i)].append(board[i][j])
                    rules['c'+str(j)].append(board[i][j])
                    rules['b'+str(i//3)+str(j//3)].append(board[i][j])
                    
        return True