from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        left = right = 0
        dq = deque()

        while right < len(nums):
            # check deque if the dq[0] is smaller than current number
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if right + 1 >= k:
                output.append(nums[dq[0]])
                left += 1

            right += 1
        return output