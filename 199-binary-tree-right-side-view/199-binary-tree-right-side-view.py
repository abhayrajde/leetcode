# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res = []
        q = deque()
        if(root):
            q.append(root)
        while(q):
            for i in range(len(q)):
                curr = q.popleft()
                val = curr.val
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            res.append(val)
        return(res)
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        