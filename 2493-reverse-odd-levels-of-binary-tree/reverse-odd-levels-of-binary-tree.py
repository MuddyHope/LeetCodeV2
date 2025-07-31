# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        curr = root
        def recursive(node1, node2, level):
            if not node1 and not node2:
                return
            if level %2 != 0:
                node1.val, node2.val = node2.val, node1.val
            
            recursive(node1.left, node2.right, level+1)
            recursive(node1.right, node2.left, level+1)
        recursive(curr.left, curr.right, 1)
        return root
    
