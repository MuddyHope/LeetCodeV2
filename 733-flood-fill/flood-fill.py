class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows_max = len(image)
        cols_max = len(image[0])

        def dfs(image, x, y, i_color, f_color):
            print(f"x: {x}, y: {y}, image: {image}")
            if (0 <= x < rows_max and 0 <= y < cols_max):
                if image[x][y] == i_color:
                    image[x][y] = f_color
                    for direction in directions:
                        dx, dy = direction
                        dfs(image, x+dx, y+dy, i_color, f_color)
            return image



        # start from sr, sc
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        return dfs(image, sr, sc, initial_color, color) 