# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.first = self.middle = self.last = None
        self.prev = TreeNode(-float("inf"))
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if(self.prev != None and (self.prev.val > node.val)):
                if not self.first:
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node
            self.prev = node
            inorder(node.right)
        
        
        inorder(root)
        
        if(self.first and self.last):
            self.first.val,self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.middle.val = self.middle.val,self.first.val
            
        
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        