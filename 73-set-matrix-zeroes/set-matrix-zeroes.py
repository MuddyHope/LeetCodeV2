class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dq = deque([])

        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    dq.append([r,c])


        while dq:
            x, y = dq.popleft()
            # for rows
            # x -> rows
            matrix[x] = [0] * (n)

            for r in range(m):
                matrix[r][y] = 0
        
        
