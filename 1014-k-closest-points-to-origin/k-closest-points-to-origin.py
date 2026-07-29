class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        nums = []
        heapq.heapify(nums)

        for x, y in points:
            heapq.heappush(nums, (self.find_dist(x,y), [x,y]))
        
        i = 0
        res = []
        while i < k:
            res.append(heapq.heappop(nums)[1])
            i += 1
        
        return res

    
    def find_dist(self, x, y):
        return math.sqrt((x-0) ** 2 + (y-0) ** 2)