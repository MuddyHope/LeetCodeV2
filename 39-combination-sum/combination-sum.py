class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # backtrack by adding itself or adding the next
        subset = []
        def dfs(i):
            if i >= len(candidates):
                return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif sum(subset) > target:
                return

            subset.append(candidates[i])

            # adding itself
            dfs(i)

            # adding the next integer
            subset.pop()
            dfs(i+1)


        dfs(0)
        return res
        
