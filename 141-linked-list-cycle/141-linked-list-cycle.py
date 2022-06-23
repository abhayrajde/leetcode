# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        hs = set()
        curr = head
        while(curr):
            if(curr in hs):
                return(True)
            hs.add(curr)
            curr = curr.next
        return(False)
        
        """
        :type head: ListNode
        :rtype: bool
        """
        