class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        max_len = 0

        def bfs(row, col):
            all_direc = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
            q=[]
            size = 1
            q.append([row, col])
            visited.add((row, col))
            while q:
                row, col=q.pop()

                for dir_r, dir_c in all_direc:
                    new_r, new_c = row + dir_r, col + dir_c

                    if(new_r in range(len(grid)) and
                        new_c in range(len(grid[0])) and
                        grid[new_r][new_c]==1 and
                        (new_r, new_c) not in visited):

                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
                        size+=1
            return size

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i, j) not in visited:
                    length = bfs(i, j)
                    max_len = max(max_len, length)
        return max_len
