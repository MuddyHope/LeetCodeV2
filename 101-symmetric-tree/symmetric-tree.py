# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, node1=None, node2=None):
#         self.val = val
#         self.node1 = node1
#         self.node2 = node2
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not (node1 or node2):
                return True
            
            if not node1 or not node2:
                return False
            print(f"node1: {node1.val}, node2: {node2.val}")

            if node1.val != node2.val:
                print(f"returning for different values")
                return False
            
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        return dfs(root.left, root.right)
