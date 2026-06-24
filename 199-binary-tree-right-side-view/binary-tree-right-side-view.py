# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        hash_map = defaultdict(list)
        max_level = 0
        # dfs 
        def dfs(node, level):
            nonlocal max_level
            if not node:
                return None, level

            right = dfs(node.right, level+1)
            left = dfs(node.left, level+1)

            max_level = max(level+1, max_level)

            if not hash_map[level]:
                hash_map[level].append(node.val)
            
            return (right or left, level)


        dfs(root, 0)
    
        for i in range(max_level):
            res.append(hash_map[i][0])
        
        return res
        
        


