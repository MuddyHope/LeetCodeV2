# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        
        l, r = 0, len(nums) -1

        def dfs(l, r):
            if not l <= r:
                return
            mid = (l+r) //2
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node
    
        return dfs(l, r)