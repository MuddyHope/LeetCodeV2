# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # traverse from head
        head_1, head_2 = l1, l2
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while head_1 or head_2 or carry:
            v1 = head_1.val if head_1 else 0
            v2 = head_2.val if head_2 else 0
            curr_sum = carry + v1 + v2
            # create new node
            carry = curr_sum // 10
            curr_sum = curr_sum % 10 

            new_node = ListNode(curr_sum)
            curr.next = new_node

            # update pointers
            curr = curr.next
            head_1 = head_1.next if head_1 else None
            head_2 = head_2.next if head_2 else None
        return dummy.next



        


