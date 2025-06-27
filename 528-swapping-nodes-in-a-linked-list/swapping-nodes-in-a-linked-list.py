# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head

        # Step 1: Find length of the list
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        print(f"total_length: {n}")

        # Step 2: Traverse again to find the nodes and their previous pointers
        prev = dummy
        curr = head

        slow_left = fast_left = slow_right = fast_right = None

        i = 1
        while curr:
            if i == k:
                slow_left = prev
                fast_left = curr
            if i == n - k + 1:
                slow_right = prev
                fast_right = curr

            prev = curr
            curr = curr.next
            i += 1

        print(f"fast_left: {fast_left.val}, fast_right: {fast_right.val}")

        # Edge case: swapping same node
        if fast_left == fast_right:
            return dummy.next

        # Step 3: Swap the nodes
        if slow_left.next == slow_right:  # Adjacent case
            slow_left.next = fast_right
            fast_left.next = fast_right.next
            fast_right.next = fast_left
        elif slow_right.next == slow_left:  # Other adjacent case
            slow_right.next = fast_left
            fast_right.next = fast_left.next
            fast_left.next = fast_right
        else:
            # Non-adjacent nodes
            temp1 = fast_left.next
            temp2 = fast_right.next

            slow_left.next = fast_right
            fast_right.next = temp1

            slow_right.next = fast_left
            fast_left.next = temp2

        return dummy.next
