# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = set()

        def dfs(root):
            if not root:
                return
            res.add(root.val)
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        res = list(res)
        res.sort()
        print(res)
        return res[1] if len(res) > 1 else -1