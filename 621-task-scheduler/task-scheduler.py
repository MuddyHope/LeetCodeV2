class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []

        counter = Counter(tasks)

        for val, i in counter.items():
            heapq.heappush(heap, (-i, val))

        res = 0
        dq = deque()  #
    
        while heap or dq:
            if dq and dq[0][2] == res:
                count, val, time = dq.popleft()
                heapq.heappush(heap, (count,val))
            
            if heap:
                count, val = heapq.heappop(heap)

                count += 1
                if count != 0:
                    dq.append((count, val, res + n + 1))
            res += 1
        return res