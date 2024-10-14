class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        region_on_edge=[]
        for i in range(len(board)):

            if board[i][0]=="O":
                region_on_edge.append([i, 0])

            if board[i][len(board[0])-1]=="O":
                region_on_edge.append([i, len(board[0])-1])
        
        for j in range(len(board[0])):

            if board[0][j]=="O":
                region_on_edge.append([0, j])
                
            if board[len(board)-1][j]=="O":
                region_on_edge.append([len(board)-1, j])
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while region_on_edge:
            x, y = region_on_edge.pop(0)
            board[x][y] = "x"
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<len(board) and 0<=new_y<len(board[0]) and board[new_x][new_y]=="O":
                    region_on_edge.append([new_x, new_y])
                    board[new_x][new_y]='x'

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="x":
                    board[i][j]="O"
        