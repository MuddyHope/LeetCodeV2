import heapq
from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_dict = []
        heap = []

        # First pass: Calculate distance and store in a dictionary list
        for i, each_point in enumerate(points):
            my_dict.append({"dist": self.cal_distance(each_point), "point": each_point})

        # Second pass: Push all dictionaries into a min-heap
        for i, each in enumerate(my_dict):
            # To prevent the TypeError, add a unique identifier (like the index 'i')
            # after the distance. This ensures that even if distances are the same,
            # the tuples will be uniquely sorted without comparing dictionaries.
            heapq.heappush(heap, (each['dist'], i, each))
        
        res = []
        # Pop the k closest points from the min-heap
        for _ in range(k):
            # The heappop operation returns a tuple (dist, index, dictionary)
            dist, _, dist_dict = heapq.heappop(heap)
            
            # Append the original point to the result list
            res.append(dist_dict.get('point'))
        
        return res
    
    def cal_distance(self, point: List[int]) -> float:
        point_x, point_y = point
        return sqrt((point_x ** 2) + (point_y ** 2))