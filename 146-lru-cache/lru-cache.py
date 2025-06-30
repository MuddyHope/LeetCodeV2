class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = {}
        # will have key, but val will be a pointer to a node
        self.cap = capacity
        # left and right are pointers
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        # remove from left
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    
    def insert(self, node: Node):
        # insert to the right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            gotten_node = self.cache.get(key)
            # now make it point as this node is Most Recently used
            # removing it from left pointer
            self.remove(gotten_node)
            # inserting to the right of the right pointer
            self.insert(gotten_node)
            res = gotten_node.val
        else:
            res = -1
        
        return res
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)