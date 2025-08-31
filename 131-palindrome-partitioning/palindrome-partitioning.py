class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def is_palindrome(self, word, first, last):
        res = True
        while first <= last:
            if word[first] != word[last]:
                return False
            else:
                first += 1
                last -= 1
        return res
        
                