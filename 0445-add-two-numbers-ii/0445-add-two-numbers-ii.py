# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # without reverse
        
        sck1, sck2 = [], []
        while l1:
            sck1.append(l1.val)
            l1 = l1.next
        
        while l2:
            sck2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        
        while sck1 or sck2 or carry:
            dig1 = 0
            dig2 = 0
            dig1 = sck1.pop() if sck1 else 0
            dig2 = sck2.pop() if sck2 else 0
            
            # new_number = dig1 + dig2 + carry
            carry, digit = divmod(dig1 + dig2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new
        return head
            
#         # reverse l1 and l2
#         curr1 = l1
#         curr2 = l2
#         prev1 = prev2 = None
        
#         while curr1:
#             temp = curr1.next
#             curr1.next = prev1
#             prev1 = curr1
#             curr1 = temp 
        
#         while curr2:
#             temp = curr2.next
#             curr2.next = prev2 
#             prev2 = curr2
#             curr2 = temp
        
#         res = l3 = ListNode(0)
#         carry = False
#         while prev1 and prev2:
#             if carry:
#                 value = 1 + prev1.val + prev2.val
#                 carry = False
#             else:
#                 value = prev1.val + prev2.val

#             if value >= 10:
#                 carry = True
#             l3.val = value%10
#             prev1 = prev1.next
#             prev2 = prev2.next
#             if prev1 or prev2:
#                 l3.next = ListNode(0)
#                 l3 = l3.next
            
        
#         while prev1:
#             if carry:
#                 value = 1 + prev1.val
#                 carry = False
#             else:
#                 value = prev1.val
#             l3.val += value
#             if value >= 10:
#                 carry = True
#             l3.val = value%10
#             prev1 = prev1.next
#             if prev1:
#                 l3.next = ListNode(0)
#                 l3 = l3.next
        
#         while prev2:
#             if carry:
#                 value = 1 + prev2.val
#                 carry = False
#             else:
#                 value = prev2.val
#             l3.val += value
#             if value >= 10:
#                 carry = True
#             l3.val = value%10
#             prev2 = prev2.next
#             if prev2:
#                 l3.next = ListNode(0)
#                 l3 = l3.next
        
#         if carry:
#             l3.next = ListNode(1)
            
#         curr = res
#         prev = None
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp 
#         return prev
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        