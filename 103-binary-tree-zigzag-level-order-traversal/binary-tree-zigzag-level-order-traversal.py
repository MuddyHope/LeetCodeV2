# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        dq = deque([root])

        res = []
        if not root:
            return res
        i = 0

        while dq:
            print(f"dq: {dq}")
            temp = []
            for _ in range(len(dq)):
                curr = dq.popleft()
                temp.append(curr.val)
                if curr.right:
                    dq.append(curr.right)
                if curr.left:
                    dq.append(curr.left)
            # print(f"temp: {temp}")
            if i % 2 == 0:
                res.append(temp[::-1])
            else: 
                res.append(temp)
            i += 1
        return res
            
