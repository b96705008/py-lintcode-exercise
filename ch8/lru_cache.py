class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.move_to_tail(node)
        return node.val
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        node = None
        if key not in self.hash_map:
            if self.is_full():
                self.remove_first()
            node = Node(key, value)
            self.hash_map[key] = node
        else:
            node = self.hash_map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            
        self.move_to_tail(node)
        
    
    def is_full(self):
        return len(self.hash_map) >= self.capacity
    
    
    def move_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
    
    
    def remove_first(self):
        node = self.head.next
        if node == self.tail:
            return
        self.head.next = node.next
        self.head.next.prev = self.head
        del self.hash_map[node.key]