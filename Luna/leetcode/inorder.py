##inorder
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if node is not None:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(root)
        return result

##preorder
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if node is not None:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return result
##postorder
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if node is not None:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)
        dfs(root)
        return result
