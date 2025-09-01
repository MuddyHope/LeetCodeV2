class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        negDiag = set()
        posDiag = set()

        board = [["."]*n for row in range(n)]
        print(board)
        res = 0

        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for col in range(n):
                if col in col_set or (row+col) in negDiag or (row-col) in posDiag:
                    continue
                
                board[row][col] = "Q"
                col_set.add(col)
                negDiag.add(row+col)
                posDiag.add(row-col)

                backtrack(row+1)

                board[row][col] = "."
                col_set.remove(col)
                negDiag.remove(row+col)
                posDiag.remove(row-col)
            
        backtrack(0)
        return res