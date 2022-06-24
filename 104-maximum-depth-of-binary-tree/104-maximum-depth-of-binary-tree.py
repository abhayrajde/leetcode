# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        # Recursive DFS solution for the given problem
        if not root:
            return (0)
        return(1+max(self.maxDepth(root.left),self.maxDepth(root.right)))
        """
        
        """
        # BFS solution
        if (not root):
            return(0)
        
        levels = 0
        q = deque([root])
        while(q):
            for i in range(len(q)):
                curr = q.popleft()
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            levels += 1
        return(levels)
        """
        
        # Iterative DFS Solution
        if(not root):
            return(0)
        
        stack = [[root, 1]]
        res = 1
        while(stack):
            node, height = stack.pop(0)
            
            if(node):
                res = max(res,height)
                stack.append([node.left, height+1])
                stack.append([node.right,height+1])
        return(res)
                
        
        
        """
        :type root: TreeNode
        :rtype: int
        """
        