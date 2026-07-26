# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _len = 0
        vals = []

        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            _len += 1
        

        i, j = 0, len(vals)-1
        while i < j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True
        