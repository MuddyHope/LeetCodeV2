# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Your solution here
        new_head = ListNode()
        head = new_head
        # traverse list 1
        while list1 and list2:
            if list1.val > list2.val:
                new_head.next = list2
                list2 = list2.next
            elif list2.val >= list1.val:
                new_head.next = list1
                list1 = list1.next
            new_head = new_head.next

        while list1:
            new_head.next = list1
            list1 = list1.next
            new_head = new_head.next

        while list2:
            new_head.next = list2
            list2 = list2.next
            new_head = new_head.next

        return head.next
