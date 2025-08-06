from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        dq = deque([root])
        i = 0
        while dq:
            cur_res = []
            if i % 2 == 0:
                odd = -1
            else:
                odd = 1
            for _ in range(len(dq)):
                curr = dq.popleft()
                if not curr:
                    continue
                print(f"curr: {curr.val}")
                if curr.right:
                    dq.append(curr.right)
                if curr.left:
                    dq.append(curr.left)
                cur_res.append(curr.val)
            i += 1
            res.append(cur_res[::odd])
        return (res)
        
                