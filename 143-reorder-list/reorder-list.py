# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        Do not return anything, modify head in-place instead.
        """
        # find mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid is slow.next

        # now reverse the second half
        second = slow.next  # 3
        prev = slow.next = None # None
        while second:
            temp = second.next # 4 # 5
            second.next = prev  # 3 -> None # 4 -> 3 -> None
            prev = second # 3   # 4
            second = temp   # 4 # 5
        # print_list(prev)
        # [5] -> [4] -> None

        # print_list(head)
        # [1] -> [2] -> [3] -> None

        # now we have to merge it
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next  # 2, 4 # None, 3
            first.next = second # 1->5  # 2->4
            second.next = temp1 # 1->5->2   #4->None
            first, second  = temp1, temp2   # 2, 4 # None, 3





