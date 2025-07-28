class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    
    def insert(self, node):
        right, prev = self.right, self.right.prev

        prev.next = node
        node.prev = prev
        node.next = right
        right.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        if self.cap == len(self.cache):
            lru = self.left.next
            self.remove(lru)
            lru_key = lru.key
            del self.cache[lru_key]
        mru = Node(key, value)
        self.cache[key] = mru
        self.insert(mru)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)