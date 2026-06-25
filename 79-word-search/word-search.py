class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        rows_max = len(board)
        cols_max = len(board[0])
        word_found = False
        seen = set()

        def dfs(x, y, i, curr):
            nonlocal word_found
            
            curr += board[x][y]
            # print(f"x: {x}, y: {y}, letter: {board[x][y]}, curr: {curr}")
            if curr == word:
                word_found = True
                return
            
            seen.add((x,y))

            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if (0 <= nx < rows_max and 0 <= ny < cols_max) and (i+1 < len(word)) and (board[nx][ny] == word[i+1]) and (nx,ny) not in seen:
                    dfs(nx, ny, i+1, curr)
            seen.remove((x,y))



        for x in range(rows_max):
            for y in range(cols_max):
                if word[0] == board[x][y] and not word_found:
                    dfs(x, y, 0, "")
        
        return word_found