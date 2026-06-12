class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1

        max_area = 0

        while i < j:

            area_so_far = min(height[j],height[i]) * (j-i)
            if area_so_far > max_area:
                max_area = area_so_far
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area