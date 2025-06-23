# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        # brute force method
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        vals = sorted(vals)
        dummy = new_head = ListNode()

        for each in vals:
            new_node = ListNode(each)
            new_head.next = new_node  # Link it
            new_head = new_node       # Move the pointer forward

        return dummy.next
