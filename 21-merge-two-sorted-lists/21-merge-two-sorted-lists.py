# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp = ListNode()
        op = temp
        while(l1 and l2):
            if(l1.val>=l2.val):
                op.next = l2
                l2 = l2.next
            else:
                op.next = l1
                l1 = l1.next
            op = op.next
            
        if(l1):
            op.next = l1
        else:
            op.next = l2
        return(temp.next)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        temp = ListNode()
        op = temp
        while(l1 and l2):
            if(l1.val<=l2.val):
                op.next = l1
                l1 = l1.next
                
            elif(l1.val>l2.val):
                op.next = l2
                l2 = l2.next
            op = op.next # here we will store None in op
            #print(op)
        
        if(l1):
            op.next = l1
                
        
        elif(l2):
            op.next = l2
            
        return(temp.next)
        """
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        