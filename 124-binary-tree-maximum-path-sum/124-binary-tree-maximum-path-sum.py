# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        node = root
        res = [node.val]
        
        def dfs(node):
            if not node:
                return 0 
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)
            
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)
            res[0] = max(res[0], (node.val + leftmax + rightmax))
            
            return(max((node.val + leftmax),(node.val + rightmax)))
        dfs(node)
        return(res[0])
        
        
        
        
        """
        :type root: TreeNode
        :rtype: int
        """
        