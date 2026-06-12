class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        # [[1,3], [2,5], [6,9]]

        res = [intervals[0]]
        i = 1
        while i < len(intervals):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
            i += 1
        return res





        

        
