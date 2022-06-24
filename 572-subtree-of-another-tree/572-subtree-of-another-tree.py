# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if( not subRoot):
            return(True)
        if(not root):
            return(False)
        if(self.SameTree(root,subRoot)):
            return(True)
        return(self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        
        
    def SameTree(self,root,subRoot):
        if(not root and not subRoot):
            return(True)
        
        if(not root or not subRoot):
            return(False)
        
        if(root.val != subRoot.val):
            return(False)
        
        if(self.SameTree(root.left,subRoot.left) and self.SameTree(root.right,subRoot.right)):
            return(True)
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        