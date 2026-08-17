class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        # crs, pre
        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
        
        deg = [0] * numCourses
        print(f"adj_list: {adj_list}")

        for pre in adj_list:
            for crs in adj_list[pre]:
                deg[crs] += 1
        print(deg)

        dq = deque()
        print(f"dq: {dq}")
        for i in range(numCourses):
            if deg[i] == 0:
                dq.append(i)
        
        res = []

        while dq:
            curr = dq.popleft()
            print(f"curr: {curr}")
            res.append(curr)

            for i in adj_list[curr]:
                deg[i] -= 1

                if deg[i] == 0:
                    dq.append(i)
        
        return res if len(res) == numCourses else []
