class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        prev_end = float("-inf")
        res = 0

        for start, end in intervals:
            print(f"start: {start}, end: {end}, prev_end: {prev_end}")
            if start < prev_end:
                res += 1
            else:
                prev_end = end

        return res