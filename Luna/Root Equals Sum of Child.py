class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.val == root.left.val + root.right.val: return True
        else: return False