class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer approach
        n = len(height)
        l, r = 0, n-1
        max_amt = 0
        while l <= r:
            curr_max = (r-l) * min(height[l], height[r])
            max_amt = max(curr_max, max_amt)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_amt