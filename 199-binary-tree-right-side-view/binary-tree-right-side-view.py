from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        dq = deque([root])

        while dq:
            cur_res = []
            for _ in range(len(dq)):
                each = dq.popleft()
                if not each:
                    continue
                dq.append(each.right)
                dq.append(each.left)
                cur_res.append(each.val)
            if cur_res:
                res.append(cur_res[0])
        return res
                