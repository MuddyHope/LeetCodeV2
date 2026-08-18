# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False
        def backtrack(node, curr_sum):
            nonlocal res
            if not node:
                return True
            
            curr_sum += node.val
            # print(f"curr: {node.val}")

            if curr_sum == targetSum and not node.left and not node.right:
                res = True
                return

            backtrack(node.left, curr_sum)
            backtrack(node.right, curr_sum)
            curr_sum -= node.val
        backtrack(root, 0)
        return res
            
