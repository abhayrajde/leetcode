# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        q = deque([root])
        count = 0
        
        while q:
            count+=1
            for i in range(len(q)):
                cur = q.popleft()
                
                # if both -> left and right of the node are empty--return count
                if(not cur.left and not cur.right):
                    return(count)
                if(cur.left):
                    q.append(cur.left)
                if(cur.right):
                    q.append(cur.right)
            # count+=1
        return(count)
        
        """
        :type root: TreeNode
        :rtype: int
        """
        