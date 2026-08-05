# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def dfs(curr):
            if not curr:
                return None
            # print(f"curr: {curr.val}")

            if curr.val == p.val or curr.val == q.val:
                return curr
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left and right:
                return curr
            else:
                return left or right
        
        return dfs(root)

