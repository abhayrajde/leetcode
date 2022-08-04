"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if not root:
            return
        
        q = deque([root])
        res = []
        while(q):
            qlen = len(q)-1
            for i in range(len(q)):
                curr = q.popleft()
                
                # Logic for populating the last term with null
                if(i != qlen):
                    curr.next = q[0]
                else:
                    curr.next = None
                    
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        return(root)
        """
        :type root: Node
        :rtype: Node
        """
        