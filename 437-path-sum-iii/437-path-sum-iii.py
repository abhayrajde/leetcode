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
            currsum += node.val
            if(currsum == targetSum):
                count = 1
            
            count+=dfs2(node.left,currsum)
            count+=dfs2(node.right, currsum)
            
            return(count)
        return(dfs(root,0))
            
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        