class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
    
        def dfs(temp):
            if len(temp) > len(nums):
                return

            if len(temp) == len(nums):
                res.append(temp[:])


            for j in range(len(nums)):
                if nums[j] not in temp:
                    temp.append(nums[j])
                    dfs(temp)
                    temp.pop()                

        dfs([])
        return res