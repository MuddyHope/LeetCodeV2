class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create all nodes and store them in a hashmap
        hash_map = {}

        curr = head
        while curr:
            # create a new node
            copy = Node(curr.val)
            hash_map[curr] = copy
            curr = curr.next

        old_nodes = head
        while old_nodes:
            # fetch new node from old node as hash-map
            new_node = hash_map[old_nodes]
            new_node.next = hash_map.get(old_nodes.next)
            new_node.random = hash_map.get(old_nodes.random)
            old_nodes = old_nodes.next
        return hash_map[head]


        