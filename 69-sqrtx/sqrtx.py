class Solution:
    def mySqrt(self, x: int) -> int:
        # try using binary search
        l, r = 1, x
        mid = (l+r)//2
        if x == 0:
            return 0
        if x == 1:
            return 1
        while l <= r:
            mid = (l+r)//2
            curr_square = mid * mid
            if curr_square == x:
                return mid
            elif curr_square > x:
                r = mid-1
            else:
                l = mid+1
        return r
        