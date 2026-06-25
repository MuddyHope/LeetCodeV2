class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start from any 1, keep track of all the seen

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        res = 0
        rows_max = len(grid)
        cols_max = len(grid[0])
        seen = set()

        def dfs(row, col, res):
            if not (0 <= row < rows_max and 0 <= col < cols_max):
                return
        
            if (row, col) in seen:
                return
            
            if grid[row][col] == "0":
                return
            
            seen.add((row,col))

            for dx,dy in directions:
                nx, ny = row+dx, col+dy
                dfs(nx, ny, res)
            return
            

        for row in range(rows_max):
            for col in range(cols_max):
                if (row,col) not in seen and grid[row][col] == "1":
                    res += 1
                    dfs(row,col, res)
        return res