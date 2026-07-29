class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key= lambda x:  x[0])
        stack = []

        for start, end in intervals:
            # print(f"curr: {start,end} stack : {stack}")
            if stack and stack[-1][1] >= start:
                _start, _end = stack.pop()
                stack.append([_start, max(_end, end)])
            else:
                stack.append([start,end])
        return stack