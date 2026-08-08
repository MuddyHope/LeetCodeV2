# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        res = []
        dq = deque([root])

        while dq:
            # print(f"stack: {dq}")
            temp = []
            for i in range(len(dq)):
                curr = dq.popleft()
                if not curr:
                    continue
                temp.append(curr.val)
                # print(f"curr_val: {curr.val}")
                if curr.right:
                    dq.append(curr.right)
                if curr.left:
                    dq.append(curr.left)
            if temp:
                res.append(temp[0])
        
        return res
            

