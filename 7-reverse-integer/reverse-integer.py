class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0

        if negative:
            x = str(x)[1:][::-1]
        else:
            x = str(x)[::-1]

        result = -int(x) if negative else int(x)

        if result < -(2**31) or result > 2**31 - 1:
            return 0

        return result