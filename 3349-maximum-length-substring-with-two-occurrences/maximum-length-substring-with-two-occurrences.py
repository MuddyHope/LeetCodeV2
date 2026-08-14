class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        l = res = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while count[c] > 2:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res