class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or total > target:
                return
            subset.append(candidates[i])
            # adding next value
            dfs(i+1, subset, total+candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subset, total)
        dfs(0, subset, 0)
        # print(res)
        return res
            
