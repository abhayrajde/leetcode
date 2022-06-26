# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if(not root):
            return([])
        op = [[root.val]]
        node = deque([root])
        
        while(node):
            nlen = len(node)
            temp = []
            for i in range(nlen):
                curr = node.popleft()
                if(curr.left):
                    temp.append(curr.left.val)
                    node.append(curr.left)
                if(curr.right):
                    temp.append(curr.right.val)
                    node.append(curr.right)
            if(temp):
                op.append(temp)
        return(op)
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        