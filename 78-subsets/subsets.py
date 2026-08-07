class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()
        def dfs(temp):
            # print(f"curr temp: {temp}")
            if tuple(sorted(temp)) in seen:
                return

            res.append(temp[:])
            seen.add(tuple(sorted(temp)))

            for i in range(len(nums)):
                # print(f"nums[i]: {nums[i]}")
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(temp)
                temp.pop()
    
        
        dfs([])
        return res