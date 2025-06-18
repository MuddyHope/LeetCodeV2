class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []    # temp, day
        
        i = 0
        
        while i < len(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                curr, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temperatures[i], i))
            i += 1
        return res