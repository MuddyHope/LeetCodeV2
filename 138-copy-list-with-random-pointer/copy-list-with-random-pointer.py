"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash_map = {head: Node(head.val)}

        curr = head
        while curr:
            # iterate over the linked-list
            if curr not in hash_map:
                hash_map[curr] = Node(curr.val)
            curr = curr.next
        
        # print(hash_map)
        curr = head
        while curr:
            # new_node.next -> 
            hash_map[curr].next = hash_map[curr.next] if curr.next else None
            hash_map[curr].random = hash_map[curr.random] if curr.random else None
            curr = curr.next
        return hash_map[head]