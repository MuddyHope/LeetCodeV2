# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        vals = []

        while head:
            vals.append(head.val)
            head = head.next
        
        dummy = ListNode(0)
        head = dummy

        vals.sort()
        for each in vals:
            dummy.next = ListNode(each)
            dummy = dummy.next
        
        return head.next
