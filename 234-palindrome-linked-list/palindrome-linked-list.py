# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        res = []
        while head:
            res.append(head.val)
            head = head.next

        n = len(res)
        mid = n // 2
        if n % 2 == 0:
            return res[:mid] == res[mid:][::-1]
        else:
            return res[:mid] == res[mid+1:][::-1]