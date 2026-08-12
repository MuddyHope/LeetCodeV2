# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.vals = []
        def dfs(node):
            if not node:
                return
            self.vals.append(node.val)
            # print(f"node: {node.val}, self.count: {self.count}, vals: {vals}")

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return sorted(self.vals)[k-1]
        # return sorted(vals)[k-1]