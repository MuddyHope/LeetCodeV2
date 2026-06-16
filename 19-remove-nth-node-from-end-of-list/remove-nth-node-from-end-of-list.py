# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        total_len = 1
        dummy = head
        while dummy and dummy.next:
            dummy = dummy.next
            total_len += 1
        
        print(total_len)
        # to be removed = total_len - n + 1

        to_be_removed = total_len - n + 1

        i = 1
        prev = None
        curr = head

        while curr:
            if i == to_be_removed:
                if prev is None:
                    return head.next

                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            i += 1
        return head