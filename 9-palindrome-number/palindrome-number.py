class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y = str(x)
        return str(x) == y[::-1]