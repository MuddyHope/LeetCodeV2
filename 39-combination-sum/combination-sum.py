class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            elif curr_sum > target or i == len(candidates):
                return
            
            dfs(i+1, curr_sum)
            sol.append(candidates[i])
            dfs(i, curr_sum + candidates[i])
            sol.pop()
        
        dfs(0, 0)
        return res
