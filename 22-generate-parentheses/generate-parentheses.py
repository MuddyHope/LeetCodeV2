class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(sol, open, close):
            print(f"sol: {sol}, open: {open}, close: {close}")
            if open == n and close == n:
                res.append("".join(sol))
                return
            

            
            if 0 <= open < n and close != n:
                sol.append("(")
                dfs(sol, open+1, close)
                sol.pop()
            if 0 <= close < n and close + 1 <= open:
                sol.append(")")
                dfs(sol, open, close+1)
                sol.pop()
            return
        

        dfs([], 0, 0)
        return res
                