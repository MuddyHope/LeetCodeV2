class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row_max = len(mat)
        col_max = len(mat[0])

        q = []

        for x in range(row_max):
            for y in range(col_max):
                if mat[x][y] == 0:
                    q.append((x,y))
                else:
                    mat[x][y] = "#"

        for r, c in q:

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx = r + dx
                ny = c + dy
                if 0 <= nx < row_max and 0 <= ny < col_max and mat[nx][ny] == "#":
                    mat[nx][ny] = 1 + mat[r][c]
                    q.append((nx,ny))
        return mat