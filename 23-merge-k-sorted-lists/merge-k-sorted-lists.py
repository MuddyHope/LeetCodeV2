# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final_list = []

        for list in lists:
            head = list
            while head:
                final_list.append(head.val)
                head = head.next
        
        # print(final_list)
        final_list.sort()
        
        dummy = ListNode(0)
        head = dummy
        for i in final_list:
            head.next = ListNode(i)
            head = head.next
        
        return dummy.next

