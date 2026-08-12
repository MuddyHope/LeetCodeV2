class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for ed1, ed2 in edges:
            graph[ed1].append(ed2)
            graph[ed2].append(ed1)

            degree[ed1] += 1
            degree[ed2] += 1

        dq = deque([])

        for node in graph:
            if degree[node] == 1:
                dq.append(node)

        remaining = n

        while remaining > 2:
            size = len(dq)
            remaining -= size

            for _ in range(size):
                curr = dq.popleft()

                for neighbor in graph[curr]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        dq.append(neighbor)

        return list(dq)