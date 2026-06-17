class Solution:
    def longestPalindrome(self, s: str) -> int:
        

        counter = defaultdict(int)
        res = 0

        for c in s:
            counter[c] += 1
            if counter[c] % 2 == 0:
                res += 2
            
        for c in counter:
            if counter[c] % 2:
                res += 1
                break
        return res