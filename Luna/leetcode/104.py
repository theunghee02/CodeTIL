class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)
        return max(a,b) +1