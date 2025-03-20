class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_copy = {str(i): 0 for i in range(10)}

        def line_checker(line):
            temp = my_copy.copy()
            for each in line:
                if each == ".":
                    continue
                temp[each] += 1
                if temp[each] > 1:
                    return False
            return True

        # check for each row
        for each_row in range(len(board)):
            row_check = line_checker(board[each_row])
            if not row_check:
                return False

        # keep the row common, keep changing the cols only
        col = 0
        while col < len(board):
            cols = []
            row = 0
            while row < len(board):
                cols.append(board[row][col])
                row += 1
            cols_checker = line_checker(cols)
            if not cols_checker:
                return False
            col += 1

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                submatrix = [board[row][col] for row in range(row_start, row_start+3) for col in range(col_start, col_start+3)]
                res = line_checker(submatrix)
                if not res:
                    return False
                # submatrices.append(submatrix)
        return True



                