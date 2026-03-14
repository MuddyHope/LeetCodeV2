from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        dq = deque()

        l, r = 0, 0

        while r < len(nums):

            # maintain decreasing deque
            while dq and dq[-1] < nums[r]:
                dq.pop()

            dq.append(nums[r])

            # when window size hits k
            if r - l + 1 == k:

                res.append(dq[0])

                # remove outgoing element
                if nums[l] == dq[0]:
                    dq.popleft()

                l += 1

            r += 1

        return res