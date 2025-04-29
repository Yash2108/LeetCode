class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        we have nxn grid
        1 is land
        0 is water
        we can start at lets say 0,0
        do bfs
        have a counter to count num of islands
        add all the elements in neighboring slots with 1 as visited and rest as seen
        when no more neighbors to be visited, we stop and increment our counter 
        '''

        num_of_islands = 0
        seen = set()
        directions = [
            [1, 0], [-1, 0], [0, -1], [0, 1]
        ]

        def bfs(row, column):
            to_visit = [ [ row, column ] ]
            seen.add( ( row, column ) )
            while to_visit:
                current_r, current_c = to_visit.pop(0)
                for dr, dc in directions:
                    new_row = current_r + dr
                    new_col = current_c + dc

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and \
                        grid[ new_row ][ new_col ] == "1" and \
                        ( new_row, new_col ) not in seen :

                        to_visit.append( [ new_row, new_col ] )
                        seen.add( ( new_row, new_col ) )

        for row in range( len( grid ) ):
            for column in range( len( grid[0] ) ):
                if ( row, column ) not in seen and grid[row][column]=="1":
                    bfs(row, column)
                    num_of_islands += 1

        return num_of_islands