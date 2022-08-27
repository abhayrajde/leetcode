# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        q = deque([root])
        reverse = False
        res = []
        while(q):
            temp = []
            for i in range(len(q)):
                curr = q.popleft()
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            if(reverse):
                temp = temp[::-1]
                res.append(temp)
                reverse = False
            else:
                res.append(temp)
                reverse = True
        return res
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        