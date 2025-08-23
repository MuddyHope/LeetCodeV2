class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # it should be a set of lists which will be converted to lists of lists later
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            # to be included
            dfs(i+1)

            # not to be included
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


