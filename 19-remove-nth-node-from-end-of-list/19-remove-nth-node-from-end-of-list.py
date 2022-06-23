# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = l = r = ListNode(0,head)
        count = -1
        
        #move right pointer till the value of n+1
        while(count < n):
            r = r.next
            count+=1
        
        while(r):
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return(dummy.next)
        
        # if(count == )
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        