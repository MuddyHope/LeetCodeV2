class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) -1
        while start <= end:
            # now swap
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
