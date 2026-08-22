class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1

        top = 0
        bottom = n
        right = n
        left = 0

        while top < bottom and left < right:

            for i in range(left, right):
                # print(f"i: {i}, left: {left}, right: {right}, top: {top}, bottom: {bottom}")

                left_top = temp = matrix[top][i]
                right_top = matrix[i][right]
                bottom_right = matrix[bottom][right - (i - left)]
                bottom_left = matrix[bottom - (i - left)][left]

                # print(left_top, right_top, bottom_right, bottom_left)

                matrix[bottom - (i - left)][left] = bottom_right
                matrix[top][i] = bottom_left
                matrix[i][right] = left_top
                matrix[bottom][right - (i - left)] = right_top

                # print(f"matrix: {matrix}")

            top += 1
            left += 1
            bottom -= 1
            right -= 1