class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.val == 0 : return False
        elif root.val == 1 : return True
        b1 = self.evaluateTree(root.left)
        b2 = self.evaluateTree(root.right)
        if root.val == 2: return b1 or b2
        else :return b1 and b2 