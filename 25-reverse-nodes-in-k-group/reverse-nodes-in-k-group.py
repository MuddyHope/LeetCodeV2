# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Assuming ListNode class is defined as above

    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while True:
            # Step 1: Check if there are k nodes remaining
            curr = prev_group_tail
            for _ in range(k):
                curr = curr.next
                if not curr: # Not enough nodes left
                    return dummy.next

            # Step 2: Identify the boundaries of the current group
            head_of_group = prev_group_tail.next
            tail_of_group_next = curr.next # This is the node AFTER the current k-group

            # Step 3: Reverse the current k-group using the helper
            # The reverse_segment function will return the new head of the reversed group
            # and correctly set the 'next' of the original head_of_group to tail_of_group_next
            new_head_of_group = self.reverse_segment(head_of_group, tail_of_group_next)

            # Step 4: Reconnect the reversed group to the main list
            prev_group_tail.next = new_head_of_group

            # Step 5: Update prev_group_tail for the next iteration
            # The original head_of_group is now the tail of the reversed group
            prev_group_tail = head_of_group
    
    def reverse_segment(self, head_of_segment, tail_of_segment_next):
        prev = tail_of_segment_next # The new tail of the reversed segment will point to this.
                                    # (e.g., if reversing [1,2,3] and next is 4, 1.next should be 4)
        curr = head_of_segment

        while curr != tail_of_segment_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev # prev will be the new head of the reversed segment
                