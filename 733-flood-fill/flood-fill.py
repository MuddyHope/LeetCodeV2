class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        init = image[sr][sc]

        if init == color:
            return image

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        m, n = len(image), len(image[0])

        def dfs(x, y):
            print(x, y)

            # out of bounds
            if not (0 <= x < m and 0 <= y < n):
                return

            if image[x][y] != init:
                return
    
            image[x][y] = color
            
            for dx,dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)
        
        dfs(sr,sc)
    
        return image