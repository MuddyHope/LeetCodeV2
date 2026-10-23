class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l, r = 0, len(height)-1

        res = float(-inf)
        while l < r:

            curr_area = min(height[l], height[r]) * (r-l)
            res = max(curr_area, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res