# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow = fast = head
        while(fast):
            slow = slow.next
            fast = fast.next.next
        
        #reverse the LL from halfway
        curr = slow 
        prev = None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        res = 0
        curr = prev
        while(curr):
            res = max(res,(head.val + curr.val))
            head = head.next
            curr = curr.next
        return res
        
            
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        