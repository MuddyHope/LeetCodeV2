from typing import Optional
import collections

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Map original node -> cloned node
        clone_map = {node: Node(node.val)}

        dq = collections.deque([node])

        while dq:
            curr = dq.popleft()

            for nei in curr.neighbors:
                if nei not in clone_map:
                    # Clone the neighbor
                    clone_map[nei] = Node(nei.val)
                    dq.append(nei)
                
                # Append the cloned neighbor to the cloned node’s neighbors
                clone_map[curr].neighbors.append(clone_map[nei])

        return clone_map[node]
