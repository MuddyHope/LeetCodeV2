class Solution:
    def longestPalindrome(self, s: str) -> int:
        # abccccdd -> evens can be added, in odd take the longeset one
        res = 0
        counter = Counter(s)
        has_odd = False
        for letter, count in counter.items():
            if count % 2 == 0:
                res += count
            else:
                has_odd = True
                res += count -1
        return (res + 1) if has_odd else res