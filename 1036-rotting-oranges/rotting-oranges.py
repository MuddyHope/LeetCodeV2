class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        max_rows = len(grid)
        max_cols = len(grid[0])
        dq = deque([])

        for r in range(max_rows):
            for c in range(max_cols):
                if grid[r][c] == 2:
                    dq.append([r,c])

        seen = set()
        time = -1
        while dq:
            # print(f"dq: {list(dq)}")
            for i in range(len(dq)):
                print(f"i: {i}, dq: {list(dq)}")
                r, c = dq.popleft()
                if not 0 <= r < max_rows or not 0 <= c < max_cols:
                    continue
            
                if (r,c) in seen:
                    continue
                
                # if grid[r][c] != 2:
                #     dq.append((r,c))
                print(f"before -> i: {i}, r, c: {r,c}, {grid[r][c]}")
                
                seen.add((r,c))

                for dx, dy in ([0,1], [1,0], [-1,0], [0,-1]):
                    nx, ny = r+dx, c+dy
                    if (not 0 <= nx < max_rows or not 0 <= ny < max_cols) or (nx,ny) in seen or grid[nx][ny] in (0,2):
                        continue
                    dq.append((nx,ny))
                    grid[nx][ny] = 2
                # print(f"grid: {grid}")
            time += 1
    

        for r in range(max_rows):
            for c in range(max_cols):
                if grid[r][c] == 1:
                    return -1
        return time if seen else 0

