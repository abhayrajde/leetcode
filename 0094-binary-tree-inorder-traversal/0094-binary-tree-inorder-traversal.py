# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        output = []
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            output.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return output
            
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        