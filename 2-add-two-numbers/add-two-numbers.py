# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            curr_sum = carry
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next

            if curr_sum >= 10:
                carry = 1
            else:
                carry = 0
            node = ListNode(curr_sum%10)
            head.next = node
            head = head.next
               
        
        if l1:
            head.next = l1
        
        if l2:
            head.next =l2
        return dummy.next