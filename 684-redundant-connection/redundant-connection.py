from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, parent, target):
            if node == target:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei not in visited and dfs(nei, node, target):
                    return True
            return False

        # iterate edges one by one
        for u, v in edges:
            visited = set()
            # if u and v are already connected, this edge is redundant
            if u in graph and v in graph and dfs(u, -1, v):
                return [u, v]
            # otherwise, add edge to graph
            graph[u].append(v)
            graph[v].append(u)
