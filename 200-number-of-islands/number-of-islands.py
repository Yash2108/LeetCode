class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited=set()
        num_islands=0

        def bfs(row, col):
            q = []
            all_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.pop(0)
                for dir_r, dir_c in all_directions:
                    new_r, new_c = r + dir_r, c + dir_c
                    if (new_r in range(len(grid)) and
                        new_c in range(len(grid[0])) and
                        grid[new_r][new_c] == "1" and
                        (new_r, new_c) not in visited):
                        
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i, j) not in visited:
                    bfs(i, j)
                    num_islands+=1
        return num_islands