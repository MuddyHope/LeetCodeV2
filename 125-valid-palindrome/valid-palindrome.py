class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # go with two-pointer
        # a: 97, z: 122
        left, right = 0, len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1

            elif s[left].lower() == s[right].lower() :

                left += 1
                right -= 1
            else:
                return False
        return True

        