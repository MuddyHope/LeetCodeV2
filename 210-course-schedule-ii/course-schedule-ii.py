from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build graph and in-degree array
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        # Step 2: Initialize queue with courses that have no prerequisites
        dq = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        # Step 3: Process queue
        while dq:
            node = dq.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dq.append(nei)

        # Step 4: Check if we were able to process all courses
        return res if len(res) == numCourses else []
