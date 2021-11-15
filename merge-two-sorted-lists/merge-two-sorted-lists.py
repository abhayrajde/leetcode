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
        op = []
        i = 0 # pointer for l1
        j = 0 # pointer for l2
        while(i<len(l1) or j<len(l2)):
            
            if(i == len(l1)):
                for k in range(j,len(l2)):
                    op.append(l1[k])
                break
            
            elif(j == len(l2)):
                for k in range(j,len(l2)):
                    op.append(l1[k])
                break
            
            elif(l1[i]<=l2[j]):
                op.append(l1[i])
                i+=1
            
            elif(l1[i]>l2[j]):
                op.append(l2[j])
                j+=1
        return (op)    
        """
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        