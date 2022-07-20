"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        oldtocopy = {None:None}
        
        # Iteration 1: in this we will only map the new copy nodes
        curr = head
        while(curr):
            oldtocopy[curr] = Node(curr.val)
            curr = curr.next
        
        #iteration 2: In this we will connect all the next and random nodes
        curr = head
        while(curr):
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        
        return(oldtocopy[head])
        
        """
        :type head: Node
        :rtype: Node
        """
        