class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        max_rows = len(grid)
        max_cols = len(grid[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
                        # up, down, left, right
        
        res = 0

        def bfs(row, col):
            dq = collections.deque()
            dq.append((row,col))
            seen.add((row, col))

            while dq:
                x, y = dq.popleft()
                for each_directions in directions:
                    _x, _y = each_directions
                    nx, ny = x + _x, y + _y
                    if 0 <= nx < max_rows and 0 <= ny < max_cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                        dq.append((nx, ny))
                        seen.add((nx, ny))


        for i in range(max_rows):
            for j in range(max_cols):
                if (i, j) not in seen and grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res