# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while(node and count < k):
            node = node.next
            count += 1
        if(count < k):
            return(head)
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, curr = None, head
        # count = 0
        while(count > 0):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count-=1
        return(curr, prev)
        
        
        
#         class Solution(object):
#     def reverseKGroup(self, head, k):
#         count, node = 0, head
#         while node and count < k:
#             node = node.next
#             count += 1
#         if count < k: return head
#         new_head, prev = self.reverse(head, count)
#         head.next = self.reverseKGroup(new_head, k)
#         return prev
    
#     def reverse(self, head, count):
#         prev, cur, nxt = None, head, head
#         while count > 0:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
#             count -= 1
#         return (cur, prev)
        
#         def reverse(node):
            
                
            
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        