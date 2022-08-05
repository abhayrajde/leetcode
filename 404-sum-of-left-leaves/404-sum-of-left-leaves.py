# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        res = [0]
        
        def dfs(node, res, check):
            if not node:
                return
            
            if(not node.left and not node.right and check):
                res[0] += node.val
                return
            dfs(node.left,res,True)
            dfs(node.right,res,False)
            return
        dfs(root,res,False)
        
        return(res[0])
        
        """
        :type root: TreeNode
        :rtype: int
        """
        