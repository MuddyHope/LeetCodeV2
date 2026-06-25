from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows_max, cols_max = len(mat), len(mat[0])

        dq = deque()


        for row in range(rows_max):
            for col in range(cols_max):
                if mat[row][col] == 0:
                    dq.append((row,col))
                else:
                    mat[row][col] = float("inf")
        

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            x, y = dq.popleft()

            for dx, dy in directions:
                nx, ny = dx+x, dy+y

                if (0 <= nx < rows_max and 0 <= ny < cols_max and mat[nx][ny] > mat[x][y] + 1):
                    mat[nx][ny] = 1 + mat[x][y]
                    dq.append((nx,ny))
        return mat 
                
                
