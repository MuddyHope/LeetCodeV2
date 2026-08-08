class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l +1: r]
        
        max_str = s[0]
        i = 0
        while i < len(s) -1:
            odd = helper(i, i)
            even = helper(i, i+1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
            i += 1
        
        return max_str