# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hm = {
            val: i
            for i, val in enumerate(inorder)
        }

        p_idx = 0
        def build(l, r):
            nonlocal p_idx
            if l > r:
                return None
            
            root_val = preorder[p_idx]
            p_idx += 1

            root = TreeNode(root_val)

            mid = inorder_hm[root_val]

            root.left = build(l, mid-1)
            root.right = build(mid+1, r)

            return root
        return build(0, len(preorder) -1)
            
