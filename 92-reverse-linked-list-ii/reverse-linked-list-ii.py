# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        start = head
        count = 1

        # First pass: Push values to stack
        curr = head
        while curr:
            if left <= count <= right:
                stack.append(curr.val)
            count += 1
            curr = curr.next

        # Second pass: Replace values with reversed ones
        count = 1
        curr = head
        while curr:
            if left <= count <= right:
                curr.val = stack.pop()
            count += 1
            curr = curr.next

        return head
