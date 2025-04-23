class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_ptr = n_ptr = 0
        guess = 0
        check_ongoing = False

        while h_ptr < len(haystack):
            print(f"h-> {haystack[h_ptr]}, n-> {needle[n_ptr]}")
            if haystack[h_ptr] == needle[n_ptr]:
                if not check_ongoing:
                    guess = h_ptr
                check_ongoing = True
                h_ptr += 1
                n_ptr += 1
                if n_ptr == len(needle):
                    return guess  # Found match at guess
            else:
                if check_ongoing:
                    h_ptr = guess + 1  # backtrack to next guess
                else:
                    h_ptr += 1
                guess = h_ptr
                n_ptr = 0
                check_ongoing = False

        return -1

        