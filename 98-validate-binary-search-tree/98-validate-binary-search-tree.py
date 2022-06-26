# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(node,left,right):
            if(not node):
                return(True)
            if not(node.val > left and node.val < right):
                return(False)
            
            return(valid(node.left,left,node.val) and valid(node.right,node.val,right))
        return(valid(root,float("-inf"),float("inf")))
        
        
        """
        # Wrong approach this is only checking the particular node only..
        if(not root):
            return(True)
        
        q = deque([root])
        while(q):
            curr = q.popleft()
            if(curr.left):
                if(curr.left.val<curr.val):
                    q.append(curr.left)
                else:
                    return(False)
            
            if(curr.right):
                if(curr.right.val>curr.val):
                    q.append(curr.right)
                else:
                    return(False)
        return(True)
        """
        """
        :type root: TreeNode
        :rtype: bool
        """
        