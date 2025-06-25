# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find middle node
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
        
        # print(f"total length => {i}")
        if i == 1:
            head = head.next
            return head
        mid_point = i//2
        dummy = head
        j = 0
        prev = ListNode()
        while j != mid_point:
            prev = dummy
            dummy = dummy.next
            j += 1
            # print(f"dummy.val -> {dummy.val}")
        # print(f"prev -> {prev}")

        prev.next = dummy.next
        return head