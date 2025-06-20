class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Sentinel to flush out stack
        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                # Width is from current i to previous bar in stack
                width = i if not stack else i - stack[-1][0] - 1
                curr_area = height * width
                # print(f"Pop: index={index}, height={height}")
                # print(f" -> Width: {width}, Area: {curr_area}")
                max_area = max(max_area, curr_area)
                # print(f" -> Max Area: {max_area}")
            stack.append((i, h))
            # print(f"Push: stack={stack}")
        # print(f"max-area", max_area)
        return max_area
