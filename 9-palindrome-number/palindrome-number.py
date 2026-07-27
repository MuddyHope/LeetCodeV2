class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y = ""
        z = str(x)
        n = len(str(x)) - 1
        
        while n >= 0:
            y += z[n]
            n -= 1
        
        return str(x) == y