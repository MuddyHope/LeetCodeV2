class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        freq = {i: 0 for i in range(26)}
        for each in s:
            freq[ord(each) - ord('a')] += 1
        n = len(s)
        res = [0] * n
        i, j = 0, n -1
        for letter_ord, count in freq.items():
            if count == 0:
                continue
            ch = chr(letter_ord + ord('a'))
            pairs = count // 2
            res[i:i+pairs] = [ch] * pairs
            res[j-pairs+1:j+1] = [ch] * pairs
            i += pairs
            j -= pairs
            if count % 2:
                res[n // 2] = ch   
        return "".join(res)