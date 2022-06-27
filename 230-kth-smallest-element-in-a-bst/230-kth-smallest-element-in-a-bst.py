# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def kthSmallest(self, root, k):
        
        # Iterative Way
        stack = deque([root])
        node = root
        count = 0
        arr = []
        while(stack):
            while(node):
                stack.append(node)
                node = node.left
            temp = stack.pop()
            count+=1
            if(count == k):
                return(temp.val)
            arr.append(temp.val)
            node = temp.right
            
        """
        # Recusrive Way
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
        """
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        