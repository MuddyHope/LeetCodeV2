# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        def recursion(node):
            if not node:
                return
            recursion(node.left)
            recursion(node.right)
            if node.right or node.left:
                node.left, node.right = node.right, node.left
        recursion(node)
        # print(root)
        return root