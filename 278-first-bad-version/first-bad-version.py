# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # binary search
        l, r = 1, n

        while l < r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            elif not isBadVersion(mid):
                l = mid +1
        return l