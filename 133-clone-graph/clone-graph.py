from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        dq = deque([node])
        seen = set()
        hash_map = {}

        while dq:
            curr_node = dq.popleft()

            if curr_node in seen:
                continue

            seen.add(curr_node)

            if curr_node not in hash_map:
                hash_map[curr_node] = Node(curr_node.val)

            for neigh in curr_node.neighbors:

                if neigh not in hash_map:
                    hash_map[neigh] = Node(neigh.val)

                hash_map[curr_node].neighbors.append(hash_map[neigh])

                dq.append(neigh)

        return hash_map[node]