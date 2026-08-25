class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(node, vals):

            if not node:
                return

            vals.append(node.val)

            # Check every path ending at the current node
            curr_sum = 0

            for i in range(len(vals) - 1, -1, -1):
                curr_sum += vals[i]

                if curr_sum == targetSum:
                    nonlocal res

                    res += 1

            dfs(node.left, vals)
            dfs(node.right, vals)

            # Backtrack
            vals.pop()

        dfs(root, [])

        return res