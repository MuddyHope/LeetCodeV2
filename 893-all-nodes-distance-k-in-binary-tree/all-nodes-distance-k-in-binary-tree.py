# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj_list = defaultdict(list)

        def dfs(node):
            if not node:
                return

            if node.left:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)

            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)


        dq = deque([target.val])
        visited = {target.val}

        res = []
        distance = 0

        while dq:

            # We have reached distance k
            if distance == k:
                return list(dq)

            # Process ONE level
            for _ in range(len(dq)):

                curr = dq.popleft()

                for nxt in adj_list[curr]:

                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)

            distance += 1

        return []