class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        rows_max = len(grid)
        cols_max = len(grid[0])

        dq = collections.deque()

        seen = set()

        for row in range(rows_max):
            for col in range(cols_max):
                if (row,col) not in seen and grid[row][col] == 2:
                    dq.append((row,col))
        
        time = -1
        while dq:
            for _ in range(len(dq)):
                # print(f"dq: {dq}")
                # print(f"grid: {grid}")
                x, y = dq.popleft()
                # print(f"x: {x}, y: {y}")

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < rows_max and
                        0 <= ny < cols_max and
                        grid[nx][ny] == 1
                    ):
                        grid[nx][ny] = 2
                        dq.append((nx, ny))
            time += 1
        

        for row in range(rows_max):
            for col in range(cols_max):
                if grid[row][col] == 1:
                    return -1
        return max(time, 0)
        

