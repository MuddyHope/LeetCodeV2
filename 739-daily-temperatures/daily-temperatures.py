class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []  # [temp, i]
        n = len(temperatures)
        res = [0] * (n)

        i = 0
        while i < len(temperatures):
            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append([temperatures[i], i])
            i += 1
        return res


