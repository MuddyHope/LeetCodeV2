class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # Edge case
        if n == 0:
            return 0

        # LEFT → RIGHT max
        left_2_right = []
        curr_max = 0
        for h in height:
            curr_max = max(curr_max, h)
            left_2_right.append(curr_max)
        print(left_2_right)

        # RIGHT → LEFT max
        right_2_left = []
        curr_max = 0
        for h in height[::-1]:
            curr_max = max(curr_max, h)
            right_2_left.append(curr_max)
        right_2_left = right_2_left[::-1]
        print(right_2_left)

        # Compute trapped water
        water = 0
        for i in range(n):
            water += min(left_2_right[i], right_2_left[i]) - height[i]

        return water
