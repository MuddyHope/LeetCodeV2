class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums = candidates

        seen = set()

        def dfs(i, curr_sum, temp):
            # print(f"i: {i}, curr_sum: {curr_sum}, temp: {temp}")
            if i >= len(candidates) or curr_sum > target:
                return

            if curr_sum == target and tuple(temp) not in seen:
                # print(f"adding to temp")
                res.append(temp[:])
                seen.add(tuple(temp))
        
            curr_sum += nums[i]
            temp.append(nums[i])

            for j in range(i, len(nums)):
                # print(f"j: {j}, curr_sum: {curr_sum}, temp: {temp}")
                dfs(j, curr_sum, temp)
            curr_sum -= nums[j]
            temp.pop()
            return
            

        for i in range(len(candidates)):
            print(f"I from for loop: {i}")
            dfs(i, 0, [])
        return res
        