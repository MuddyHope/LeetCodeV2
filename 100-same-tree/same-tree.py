# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def recursion(p, q):
            if not p and not q:
                return True
            # if (p and not q) or (q and not p):
            #     return False
            if p and not q or q and not p:
                return False
            print(f"p:{p.val}, q: {q.val}")

            if p.val != q.val:
                return False
           
            return recursion(p.right, q.right) and recursion(p.left, q.left)

        return recursion(p, q)
        

            

