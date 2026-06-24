# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # find root.val in inorder

        self.inorder_hm = {}
        for i in range(len(inorder)):
            self.inorder_hm[inorder[i]] = i
        
        pre_order_idx = 0
        def build(l, r):
            nonlocal pre_order_idx
            if l > r:
                return None
            
            root_val = preorder[pre_order_idx]
            pre_order_idx += 1

            root = TreeNode(root_val)

            mid = self.inorder_hm[root_val]

            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root
        l, r = 0, len(preorder) -1

        return build(l, r)     

            

