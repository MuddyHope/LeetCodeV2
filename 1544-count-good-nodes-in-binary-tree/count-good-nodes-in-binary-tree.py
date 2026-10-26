# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        self.res = 0
        dummy = TreeNode(float(-inf))

        def dfs(max_so_far, curr):
            if not curr:
                return
            # print(f"max_so_far: {max_so_far}, curr: {curr.val}")
            if max_so_far <= curr.val:
                self.res += 1
                max_so_far = curr.val
            
            dfs(max_so_far, curr.left)
            dfs(max_so_far, curr.right)
        
        dfs(float(-inf), root)
        return self.res