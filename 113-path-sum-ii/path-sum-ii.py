# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []

        def backtrack(node, curr_sum, sol):
            
            if not node:
                return
            
            curr_sum += node.val
            sol.append(node.val)
            print(f"curr: {node.val}, curr{curr_sum}, sol: {sol}")

            if curr_sum == targetSum and not node.right and not node.left:
                res.append(sol[:])
                sol.pop()
                return
            
            if node.left:
                backtrack(node.left, curr_sum, sol)
            if node.right:
                backtrack(node.right, curr_sum, sol)
            sol.pop()
        


        backtrack(root, 0, [])
        return res