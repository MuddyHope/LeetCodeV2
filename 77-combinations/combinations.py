class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res, sol = [], []

        def dfs(i):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for j in range(i, n+1):
                sol.append(j)
                dfs(j+1)
                sol.pop()
        
        dfs(1)
        return res