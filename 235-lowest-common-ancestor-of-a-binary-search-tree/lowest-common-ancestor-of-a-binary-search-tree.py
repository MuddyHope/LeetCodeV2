# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            print(f"curr root: {root.val}")
            if root.val > p.val and root.val > q.val:   # root value is smaller than both
                root = root.left
            elif root.val < p.val and root.val < q.val:     # root value is bigger than both
                root = root.right
            else:
                break
        return root
            