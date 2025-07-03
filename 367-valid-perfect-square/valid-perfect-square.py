class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # binary search from 0 to num
        l, r = 0, num

        while l <= r:
            mid = (l + r)//2
            print(l, mid, r)
            if mid ** 2 > num:
                r = mid - 1
            elif mid ** 2 < num:
                l = mid + 1
            elif mid ** 2 == num:
                return True
        return False

        