class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.sum_mat = [[0] * (cols + 1) for r in range(rows+1)]

        for each_row in range(rows):
            prefix_sum = 0
            for each_col in range(cols):
                prefix_sum += matrix[each_row][each_col]
                above = self.sum_mat[each_row][each_col + 1]
                self.sum_mat[each_row+1][each_col+1] = prefix_sum + above
            # print(self.sum_mat)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.sum_mat[row2+1][col2+1]
        left = self.sum_mat[row2+1][col1]
        above = self.sum_mat[row1][col2+1]
        top_left = self.sum_mat[row1][col1]
        return bottom_right - left - above + top_left
