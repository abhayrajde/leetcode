# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        
        res = []
        def dfs(node,currpath):
            if not node:
                return
            if(not node.left and not node.right):
                currpath+=str(node.val)
                # print currpath
                res.append(int(currpath))
                return
            dfs(node.left, currpath+str(node.val))
            dfs(node.right, currpath+str(node.val))
        dfs(root,"")
        return(sum(res))
        """
        :type root: TreeNode
        :rtype: int
        """
        