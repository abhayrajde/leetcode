"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        stack = []
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
                
            if not curr.next and len(stack) != 0:
                curr.next = stack.pop()
                curr.next.prev = curr
                
            curr = curr.next
        return head
        """
        :type head: Node
        :rtype: Node
        """
        