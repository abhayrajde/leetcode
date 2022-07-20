# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # l2 = self.reverse(l2)
        # l1 = self.reverse(l1)
        carry = 0
        totsum = curr = ListNode(0)
        while(l1 or l2 or carry):
            v1 = l1.val if(l1) else 0
            v2 = l2.val if l2 else 0
            
            #new digit
            temp = v1 + v2 + carry
            carry = temp//10
            temp = temp%10
            
            curr.next = ListNode(temp)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return(totsum.next)
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        