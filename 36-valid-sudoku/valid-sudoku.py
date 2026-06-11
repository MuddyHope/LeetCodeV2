class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        nums_checker = {i: 0 for i in range(1, 10)}

        def line_checker(nums):
            temp = nums_checker.copy()

            for each in nums:
                if each == ".":
                    continue

                if temp[int(each)] >= 1:
                    return False

                temp[int(each)] += 1

            return True

        # rows
        for row in range(9):
            if not line_checker(board[row]):
                return False

        # columns
        for col in range(9):
            col_list = []

            for row in range(9):
                col_list.append(board[row][col])

            if not line_checker(col_list):
                return False

        # 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):

                sub_matrix = []

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        sub_matrix.append(board[r][c])

                if not line_checker(sub_matrix):
                    return False

        return True