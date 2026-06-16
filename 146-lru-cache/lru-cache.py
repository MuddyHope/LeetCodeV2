class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lfu, self.mfu = Node(0,0), Node(0,0)
        self.lfu.right, self.mfu.left = self.mfu, self.lfu
    
    def remove(self, node):
        prev, nxt = node.left, node.right
        prev.right = nxt
        nxt.left = prev
    
    def insert(self, node):
        # insert to the left of the self.mfu
        prev = self.mfu.left
        self.mfu.left = node
        prev.right = node
        node.left = prev
        node.right = self.mfu


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # remove the node from it's position
        # insert the node to left of self.mfu
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            lfu = self.lfu.right
            self.remove(lfu)
            del self.cache[lfu.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)