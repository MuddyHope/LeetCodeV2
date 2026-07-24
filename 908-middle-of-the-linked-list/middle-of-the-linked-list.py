# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _len = 0

        curr = head
        while curr:
            curr = curr.next
            _len += 1
        
        i = _len//2
        
        while i != 0:
            head = head.next
            i -= 1
        return head