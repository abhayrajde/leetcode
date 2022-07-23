# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        self.bal = True
        def dfs(node):
            if(not node):
                return(0)
            left = dfs(node.left)
            right = dfs(node.right)
            if(abs(left-right) > 1):
                self.bal = False
            height = 1 + max(left,right)
            return(height)
        dfs(root)
        return(self.bal)
        
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        