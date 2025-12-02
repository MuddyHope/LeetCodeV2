class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # each element is (temp, index)
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            # while current temp is warmer than last stacked temp
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx

            # push current temp + index
            stack.append((temp, i))

        return res
