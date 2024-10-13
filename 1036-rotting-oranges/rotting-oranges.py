class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=grid
        rottens=[]
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==2:
                    rottens.append([i, j])
                elif visited[i][j]==1:
                    fresh+=1
        time=-1
        directions = [[1,0], [-1,0], [0, -1], [0, 1]]

        if fresh==0:
            return 0
        if not rottens:
            return -1

        while rottens:
            num_rottens=len(rottens)
            while num_rottens>0:
                x, y = rottens.pop(0)
                num_rottens-=1
                for dx, dy in directions:
                    i, j = x+dx, y+dy
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and visited[i][j]==1:
                        visited[i][j]=2
                        fresh-=1
                        rottens.append([i, j])
            time+=1
        if fresh==0:
            return time
        return -1
        
        