# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # DFS
        stack = [(root, 1)]
        res = 0

        while stack:

            node, level = stack.pop()
            if node:
                res = max(res, level)
                stack.append((node.left, 1+level))
                stack.append((node.right, 1+ level))
            
        return res
