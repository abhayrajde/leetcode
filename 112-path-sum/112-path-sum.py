# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        currsum = 0
        # res = False
        def dfs(node,currsum):
            if(not node):
                return False
            sum1= currsum+node.val
            if sum1 == targetSum and not node.left and not node.right:
                return(True)
            
            return (dfs(node.left,currsum+node.val) or dfs(node.right,currsum+node.val))
        return(dfs(root,currsum)) #(5,0) (4,5) (11,9) (7, 20), ()
                
        
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        