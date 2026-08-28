# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _ = []

        curr = head
        if not head:
            return None

        while curr:
            _.append(curr.val)
            curr = curr.next
        
        n = len(_)
        k = k % len(_)  
        new = _[-k:] + _[:-k]

        dummy = head = ListNode(0)

        i = 0
        while i < n:
            head.next = ListNode(new[i])
            i += 1
            head = head.next
        return dummy.next
