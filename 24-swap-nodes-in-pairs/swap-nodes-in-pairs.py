# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head   # 0 -> 1 -> 2 -> 3 -> 4
        prev = dummy    # 0

        while prev.next and prev.next.next:
            first = prev.next       # 1
            second = first.next     # 2
            nxt = second.next       # 3
            first.next = nxt        # 1 -> 3
            second.next = first     # 2 -> 1
            prev.next = second      # 0-> 2
            prev = first        # 1
        return dummy.next

