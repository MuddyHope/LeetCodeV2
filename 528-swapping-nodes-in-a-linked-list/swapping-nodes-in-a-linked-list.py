# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # traverse the list
        i = 1
        curr = head
        slow_pointer = fast_pointer = head
        left, right = ListNode(), ListNode()
        left_found = False
        while curr:
            if i == k:
                left = curr
                left_found = True
            if left_found:
                if fast_pointer.next == None:
                    right = slow_pointer
                    # now swap
                    left.val, right.val = right.val, left.val
                slow_pointer = slow_pointer.next

            fast_pointer = fast_pointer.next
            curr = curr.next
            i += 1
        return head

        

