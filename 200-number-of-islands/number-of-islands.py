class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        max_rows = len(grid)
        max_cols = len(grid[0])
        seen = set()
        def dfs(r, c):
            nonlocal res
            if not (0 <= r < max_rows) or not (0 <= c < max_cols):
                return

            if (r,c) in seen:
                return
            print(f"curr: r, c: {r,c} {grid[r][c]}")

            seen.add((r,c))
            if grid[r][c] == "0":
                return False
            
            for dx, dy in (0,1), (1,0), (0,-1), (-1,0):
                nx, ny = r+ dx, c + dy
                dfs(nx, ny)


        for r in range(max_rows):
            for c in range(max_cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    res += 1
        return res
