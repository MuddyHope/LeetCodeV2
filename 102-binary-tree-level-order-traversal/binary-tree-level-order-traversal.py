# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return res
        dq = deque([root])

        while dq:
            temp = []
            for i in range(len(dq)):
                _ = dq.popleft()
                if not _:
                    continue
                temp.append(_.val)
                dq.append(_.left)
                dq.append(_.right)
            if temp:
                res.extend([temp])
        return res
        