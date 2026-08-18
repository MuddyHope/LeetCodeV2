class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []

        def backtrack(node, curr_sum, sol):
            if not node:
                return

            sol.append(node.val)
            curr_sum += node.val

            if curr_sum == targetSum and not node.left and not node.right:
                res.append(sol[:])
                sol.pop()
                return

            backtrack(node.left, curr_sum, sol)
            backtrack(node.right, curr_sum, sol)

            sol.pop()

        backtrack(root, 0, [])
        return res