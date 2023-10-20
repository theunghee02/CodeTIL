# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isLeaf(node):
        if node is None:
            return False
        if node.left is None and node.right is None: return True
        else: return False
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        answer = 0
        if root is not None:
            if isLeaf(root.left):
                answer += root.left.val
            answer += self.sumOfLeftLeaves(root.left)
            answer += self.sumOfLeftLeaves(root.right)
        return answer