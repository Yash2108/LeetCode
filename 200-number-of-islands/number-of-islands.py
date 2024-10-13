class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands=0
        visited=set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):

            q=[]
            visited.add((row, col))
            q.append([row, col])
            while q:
                r, c = q.pop(0)
                for dx, dy in directions:
                    new_r, new_c = r+dx, c+dy
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and\
                        grid[new_r][new_c]=="1" and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        q.append([new_r, new_c])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i, j) not in visited: 
                    bfs(i, j)
                    islands+=1
        return islands

