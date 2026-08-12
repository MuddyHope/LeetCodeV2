class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row, column and box

        def line_checker(vals):
            temp = set()
            for each in vals:
                if each == ".":
                    continue
                elif each in temp:
                    return False
                else:
                    temp.add(each)
            return True

        # row checker 
        max_rows = len(board)
        max_cols = len(board[0])

        for i in range(max_rows):
            if not line_checker(board[i]):
                return False
        
        # column checker
        temp_board = defaultdict(list)
        for col in range(max_cols):
            for row in range(max_rows):
                temp_board[col].append(board[row][col])
        # print(temp_board)
        
        for i in temp_board:
            if not line_checker(temp_board[i]):
                return False
        
        temp_box = defaultdict(list)
        box_idx = 0
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                vals = []

                for i in range(row, row+3):
                    for j in range(col, col+3):
                        vals.append(board[i][j])
                if not line_checker(vals):
                    return False
        return True

                
