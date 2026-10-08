class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.dfs(root) != -1

    def dfs(self, node):

        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)