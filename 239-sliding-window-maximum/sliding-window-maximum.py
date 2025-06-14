from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()  # stores indices of nums

        for i in range(len(nums)):
            # Remove indices out of window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller values from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Add to result once window is of size k
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
