class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        n = len(temperatures)

        stack = []

        for each in range(n):

            while stack and temperatures[each] > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = (each-prev_idx)
            
            stack.append((temperatures[each], each))
        
        return res
