# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def kthSmallest(self, root, k):
        arr=[]
        self.dfs(root,arr)
        return arr[k-1]
        
        
    def dfs(self,root,arr):
        if(not root):
            return None
        self.dfs(root.left,arr)
        arr.append(root.val)
        self.dfs(root.right,arr)
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         op = root
#         if(k == 0):
#             return(op.val)
#         if(not root):
#             return
        
#         self.kthSmallest(root.left,k)
#         k = k-1
#         self.kthSmallest(root.right,k)
#         k = k-1
    
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        