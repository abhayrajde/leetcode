# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        res = [True]
        
        def dfs(node,left,right):
            if not node:
                return
            
            if node.val <= left or node.val >= right:
                res[0] = False
            
            dfs(node.left,left,node.val)
            dfs(node.right,node.val,right)
        dfs(root,float("-inf"),float("inf"))
        return res[0]
                
                
            
        """
        :type root: TreeNode
        :rtype: bool
        """
        