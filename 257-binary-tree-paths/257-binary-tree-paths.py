# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        curr = ""
        def dfs(node,curr):    
            if not node.left and not node.right:
                curr+=str(node.val)
                res.append(curr[:])
                return
            
            if node.left:
                dfs(node.left,curr+str(node.val)+"->")
            if node.right:
                dfs(node.right, curr+str(node.val)+"->")
        dfs(root,curr)
        return res
                
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        