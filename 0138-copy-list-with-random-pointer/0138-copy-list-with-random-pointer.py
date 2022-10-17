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
        oldtocopy = { None:None }
        curr = head
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            # copy.next = curr.next
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        
        return oldtocopy[head]
        

        
#         oldtocopy = {None:None}
#         curr = head
#         while curr:
#             copy = Node(curr.val)
#             oldtocopy[curr] = copy
#             curr = curr.next
        
#         curr = head
#         while curr:
#             copy = oldtocopy[curr]
#             copy.next = oldtocopy[curr.next]
#             copy.random = oldtocopy[curr.random]
#             curr = curr.next
#         return oldtocopy[head]
        """
        :type head: Node
        :rtype: Node
        """
        