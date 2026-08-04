class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums = candidates

        def dfs(i, curr_sum, temp):
            if curr_sum > target:
                return
            
            if curr_sum == target:
                res.append(temp[:])
                return
            
            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(j, curr_sum + nums[j], temp)
                temp.pop()
        

        dfs(0, 0, [])
        return res