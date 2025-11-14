class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two-pointer

        left, right = 0, len(s) - 1

        print(ord('0'), ord('9'))

        while left <= right:
            print(f"currently checking for : {s[left]}, {s[right]}")
            if not 97 <= ord(s[left].lower()) <= 122 and not 48 <= ord(s[left].lower()) <= 57:
                print(f"left: {s[left]}")
                left += 1
                continue
            if not 97 <= ord(s[right].lower()) <= 122 and not 48 <= ord(s[right].lower()) <= 57:
                print(f"right : {s[right]}")
                right -= 1
                continue

            elif s[left].lower() == s[right].lower():
                right -= 1
                left += 1
            else:
                return False
        return True
