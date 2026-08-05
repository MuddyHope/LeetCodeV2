class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        stack = []

        for _start, _end in intervals:
            if stack and stack[-1][1] >= _start:
                _ = stack.pop()
                stack.append([_[0], max(_end, _[1])])
            else:
                stack.append([_start, _end])
        return stack