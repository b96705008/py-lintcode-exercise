class Node(object):
    def __init__(self, prev=None, next=None):
        self.prev = prev
        self.next = next


class ItemNode(Node):
    def __init__(self, key, prev=None, next=None):
        super(ItemNode, self).__init__(prev, next)
        self.key = key


class FreqNode(Node):
    def __init__(self, value=0, prev=None, next=None):
        super(FreqNode, self).__init__(prev, next)
        self.value = value
        self.items = {}
        self.item_head = ItemNode(None)
        self.item_tail = ItemNode(None)
        self.item_head.next = self.item_tail
        self.item_tail.prev = self.item_head

    def is_empty(self):
        return len(self.items) == 0

    def add_last(self, key):
        # add to tail
        if key in self.items:
            return None
        current = ItemNode(key, self.item_tail.prev, self.item_tail)
        self.item_tail.prev.next = current
        self.item_tail.prev = current
        self.items[key] = current
        return current

    def remove(self, key):
        if key not in self.items:
            return False
        node = self.items[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        del self.items[key]
        return True

    def remove_first(self):
        # remove oldest
        first = self.item_head.next
        if first == self.item_tail:
            return None
        self.remove(first.key)
        return first.key


class LFUItem:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.bykey = {}
        self.freq_head = FreqNode(value=0)
        self.freq_tail = FreqNode(value=float('inf'))
        self.freq_head.next = self.freq_tail
        self.freq_tail.prev = self.freq_head

    def is_full(self):
        return len(self.bykey) == self.capacity

    def create_new_freq_node(self, value, prev, next):
        node = FreqNode(value, prev, next)
        prev.next = node
        next.prev = node
        return node

    def delete_freq_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def delete_least_used_item(self):
        # find least freq node
        freq = self.freq_head.next
        if freq == self.freq_tail:
            return False
        # remove oldest item node (like LRU)
        deleted_key = freq.remove_first()
        if deleted_key is not None:
            del self.bykey[deleted_key]
        # remove freq if it is empty
        if freq.is_empty():
            self.delete_freq_node(freq)

        return True

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.bykey:
            # equal to update + access 1 time
            self.bykey[key].value = value
            self.get(key)
            return

        # check current capacity
        if self.is_full():
            is_success = self.delete_least_used_item()
            if not is_success:
                return

        # get related freq nodes
        freq = self.freq_head.next
        if freq == self.freq_tail or freq.value != 1:
            freq = self.create_new_freq_node(1, self.freq_head, freq)

        freq.add_last(key)
        self.bykey[key] = LFUItem(value, freq)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.bykey:
            return -1

        # get item, and related freq nodes
        item = self.bykey[key]
        freq = item.parent
        next_freq = freq.next

        # update item frequence
        if next_freq == self.freq_tail or \
            next_freq.value != freq.value + 1:
            next_freq = self.create_new_freq_node(freq.value+1, freq, next_freq)
        next_freq.add_last(key)
        self.bykey[key].parent = next_freq

        # remove old freq
        freq.remove(key)
        if freq.is_empty():
            self.delete_freq_node(freq)

        return item.value


if __name__ == '__main__':
    cache = LFUCache(3)
    cache.set(2, 2)
    cache.set(1, 1)
    print cache.get(2)
    print cache.get(1)
    cache.set(3, 3)
    cache.set(4, 4)
    print cache.get(3)
    print cache.get(2)
    print cache.get(1)
    print cache.get(4)
    print cache.get(4)
    print cache.get(4)
    cache.set(5, 5)
    print cache.get(5)
    print cache.get(2)


