class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("", 0, 0)]

        res = []
        while stack:
            curr, _open, _close = stack.pop()
            if len(curr) == 2*n:
                res.append(curr)
            if _open < n:
                stack.append((curr + "(", _open+1, _close))
            if _close < _open:
                stack.append((curr + ")", _open, _close + 1))
        return res