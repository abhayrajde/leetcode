# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(node, currsum):
            if(not node):
                return(0)
            return(dfs(node.left,currsum) +
            dfs(node.right, currsum) +
            dfs2(node, currsum))
        
        def dfs2(node,currsum):
            if(not node):
                return(0)
            count = 0
            
            if(node.val == currsum):
                count = 1
            
            count+=dfs2(node.left,currsum-node.val)
            count+=dfs2(node.right, currsum-node.val)
            
            return(count)
        return(dfs(root,targetSum))
            
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        