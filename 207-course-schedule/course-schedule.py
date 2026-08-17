class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph + count prerequisites
        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            indegree[crs] += 1

        # Courses with no prerequisites
        dq = deque()

        for crs in range(numCourses):
            if indegree[crs] == 0:
                dq.append(crs)

        completed = 0

        while dq:
            curr = dq.popleft()
            completed += 1

            for crs in adj_list[curr]:
                indegree[crs] -= 1

                if indegree[crs] == 0:
                    dq.append(crs)

        return completed == numCourses