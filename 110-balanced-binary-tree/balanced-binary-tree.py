# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = 0
        def dfs(node):
            nonlocal res
            # check left height and right height
            if not node:
                return 0
            
            _left = 1 + dfs(node.left)
            _right = 1 + dfs(node.right)
            res = max(res, abs(_left - _right))
            return max(_left, _right)

        dfs(root)
        if res > 1:
            return False
        return True
        