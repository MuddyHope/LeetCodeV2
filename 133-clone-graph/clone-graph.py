"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        root = node
        dq = deque([node])

        hash_map = {}
        seen = set()

        while dq:
            curr = dq.popleft()

            if curr not in seen:
                seen.add(curr)

                if curr not in hash_map:
                    new_node = Node(curr.val)
                    hash_map[curr] = new_node
                new_node = hash_map[curr]

                for nei in curr.neighbors:
                    if nei in hash_map:
                        new_nei = hash_map[nei]
                    else:
                        new_nei = Node(nei.val)
                        hash_map[nei] = new_nei
                    new_node.neighbors.append(new_nei)
                    dq.append(nei)
        return hash_map[root]
