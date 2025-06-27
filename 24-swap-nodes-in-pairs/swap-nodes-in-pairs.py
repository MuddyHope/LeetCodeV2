class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move forward
            prev = first
            head = first.next

        return dummy.next
