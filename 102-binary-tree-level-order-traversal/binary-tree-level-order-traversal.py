from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        # for BFS use queue
        if not root:
            return res

        dq = deque([root])

        while dq:
            curr_res = []
            for i in range(len(dq)):
                print(f"dq: {i}")
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
                curr_res.append(curr.val)
                print(f"curr_res: {curr_res}")

            res.append(curr_res)
        print(res)
        return res

        