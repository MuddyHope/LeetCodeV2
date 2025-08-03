# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        # now edge cases are done, we have to check if current ROOT and SUBROOT is same
        res = self.is_same_tree(root, subRoot)
        if not res:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        return True
        
        
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            print(f"checking for : {p.val}, {q.val}")

            return (self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right))
        return False
        
