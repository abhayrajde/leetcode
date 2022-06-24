# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        
        if( not lists or len(lists)==0):
            return(None)
        
        while(len(lists)>1):
            mergelist = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if((i+1 < len(lists))):
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergelist.append(self.merge(l1,l2))
            lists = mergelist
        return(lists[0])
    
    def merge(self,l1,l2):
        temp = ListNode()
        op = temp
        while(l1 and l2):
            if(l1.val < l2.val):
                op.next = l1
                l1 = l1.next
            else:
                op.next = l2
                l2 = l2.next
            op = op.next
        if(l1):
            op.next = l1
        else:
            op.next = l2
        return(temp.next)
        #TODO
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        