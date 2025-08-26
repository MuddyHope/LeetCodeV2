class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = set()
        def dfs(curr, used):
            print(f"used: {used}, curr: {curr}")
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                curr.append(nums[i])
                dfs(curr, used)
                curr.pop()
                used.remove(i)


        dfs([], set())
        return res