class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0

        while i < len(s):

            j = i

            while j < len(s):
                
                if j - i + 1 > len(res):
                    if is_palindrome(i, j):
                        res = s[i:j+1]

                j += 1

            i += 1

        return res