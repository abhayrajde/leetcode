# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        
        def dfs(node, maxval):
            if not node:
                return 0
            
            if(node.val >= maxval):
                maxval = node.val
                res = 1
            else:
                res = 0
            res += dfs(node.left,maxval)
            res += dfs(node.right,maxval)
            return res
        return(dfs(root,root.val))
        
                
        """
        :type root: TreeNode
        :rtype: int
        """
        