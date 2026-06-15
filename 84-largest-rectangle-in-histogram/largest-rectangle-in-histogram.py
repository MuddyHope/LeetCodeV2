class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # add the minimum of curr_height and the stack[-1] height to the stack
        # if the height of the next height is smaller than the top of the stack height, pop it

        stack = []  # (idx, height)
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append([start, heights[i]])
        

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area