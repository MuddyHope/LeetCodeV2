# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        
        vals = []

        # binary tree level-by-level traversal
        dq = deque([root])

        while dq:
            temp = []
            for _ in range(len(dq)):
                curr = dq.popleft()
                # print(f"curr: {curr.val}")
                temp.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            vals.append(temp)
        return vals[-1][0]
