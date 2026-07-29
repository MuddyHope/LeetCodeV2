class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1

        # left is the insertion position
        intervals.insert(left, newInterval)
        stack = []

        for start, end in intervals:
            # print(f"curr: {start,end} stack : {stack}")
            if stack and stack[-1][1] >= start:
                _start, _end = stack.pop()
                stack.append([_start, max(_end, end)])
            else:
                stack.append([start,end])
        return stack