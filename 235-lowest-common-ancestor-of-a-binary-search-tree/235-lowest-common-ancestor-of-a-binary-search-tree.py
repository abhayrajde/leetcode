# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        while(curr):
            if(p.val > curr.val and q.val > curr.val):
                curr = curr.right
            elif(p.val < curr.val and q.val < curr.val):
                curr = curr.left
            else:
                return(curr)
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        