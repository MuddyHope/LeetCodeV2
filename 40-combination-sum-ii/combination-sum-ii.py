from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        subset = []
        
        def dfs(i):
            # Base Case 1: Target is met
            if sum(subset) == target:
                res.append(subset.copy())
                return
            
            # Base Case 2: Target is exceeded or we are out of candidates
            if sum(subset) > target or i >= len(candidates):
                return
            
            # --- Decision Point: Take the current element ---
            
            # Add the current candidate to the subset
            subset.append(candidates[i])
            
            # Recursively call with the next index (i + 1)
            dfs(i + 1)
            
            # --- Backtrack: Undo the decision to explore another path ---
            
            # Remove the last element added
            subset.pop()
            
            # --- Decision Point: Skip all duplicate elements ---
            
            # This is the key to handling duplicates. We skip any
            # consecutive elements that are the same as the one we just processed.
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            # Recursively call to explore combinations *without* the current element
            dfs(i + 1)

        dfs(0)
        return res