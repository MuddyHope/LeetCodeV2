# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        l = 0 
        r = len(nums) -1 

        def dfs(l, r):
            if not l <= r:
                return
            mid = (l+r)//2
            print(l, mid, r)
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1,r)
            return node

        return dfs(l, r)
