class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # First: Get length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # Edge case: If k > length
        if k > length:
            return head

        # Now find k-th and (length - k + 1)-th nodes and their prev
        first_prev = dummy
        for _ in range(k - 1):
            first_prev = first_prev.next
        first = first_prev.next

        second_prev = dummy
        for _ in range(length - k):
            second_prev = second_prev.next
        second = second_prev.next

        # If they're the same node, no swap needed
        if first == second:
            return dummy.next

        # Handle adjacent case
        if first.next == second:
            first_prev.next = second
            first.next = second.next
            second.next = first
        elif second.next == first:
            second_prev.next = first
            second.next = first.next
            first.next = second
        else:
            # Swap non-adjacent nodes
            first_prev.next, second_prev.next = second, first
            first.next, second.next = second.next, first.next

        return dummy.next
