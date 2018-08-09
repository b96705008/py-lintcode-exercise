class Node:

    def __init__(self, index, cnt):
        self.index = index
        self.cnt = cnt

    def update_index(self, index):
        self.index = index


class HashHeap:

    def __init__(self):
        self.min_heap = []
        self.hash_map = {}
        self.size = 0

    def parent_index(self, index):
        return (index - 1) / 2

    def left_index(self, index):
        return index * 2 + 1

    def right_index(self, index):
        return index * 2 + 2

    def empty(self):
        return self.size == 0

    def qsize(self):
        return len(self.min_heap)

    def top(self):
        return self.min_heap[0]

    def add(self, val):
        self.size += 1

        if val in self.hash_map:
            self.hash_map[val].cnt += 1
        else:
            self.min_heap.append(val)
            self.hash_map[val] = Node(self.qsize()-1, 1)
            self.shift_up(self.qsize()-1)

    def poll(self):
        self.size -= 1
        val = self.top()
        node = self.hash_map[val]

        if node.cnt == 1:
            self.swap(0, self.qsize()-1)
            self.min_heap.pop()
            del self.hash_map[val]
            if not self.empty():
                self.shift_down(0)
        else:
            node.cnt -= 1

        return val

    def delete(self, val):
        self.size -= 1
        node = self.hash_map[val]

        if node.cnt == 1:
            index = node.index
            self.swap(index, self.qsize()-1)
            self.min_heap.pop()
            del self.hash_map[val]

            # in the middlde
            if index < self.qsize():
                self.shift_up(index)
                self.shift_down(index)
        else:
            node.cnt -= 1

    def smaller(self, i1, i2):
        return self.min_heap[i1] < self.min_heap[i2]

    def swap(self, i1, i2):
        v1 = self.min_heap[i1]
        v2 = self.min_heap[i2]
        n1 = self.hash_map[v1]
        n2 = self.hash_map[v2]
        # swqp hash
        n1.update_index(i2)
        n2.update_index(i1)
        # swap heap
        self.min_heap[i1], self.min_heap[i2] = self.min_heap[i2], self.min_heap[i1]

    def shift_up(self, index):
        while index > 0:
            parent = self.parent_index(index)
            if not self.smaller(index, parent):
                break
            self.swap(index, parent)
            index = parent

    def shift_down(self, index):
        while self.left_index(index) < self.qsize():
            index
            left = self.left_index(index)
            right = self.right_index(index)

            child = left
            if right < self.qsize() and self.smaller(right, child):
                child = right

            if self.smaller(child, index):
               self.swap(child, index)
               index = child
            else:
                break


if __name__ == '__main__':
    hh = HashHeap()
    hh.add(1)
    #print hh.top()

    hh.add(80)
    #print hh.top()

    hh.add(60)
    #print hh.top()

    hh.add(90)
    hh.add(70)
    hh.add(75)
    hh.add(100)
    hh.add(150)

    print hh.poll()
    hh.delete(90)

    print hh.poll()
    print hh.poll()

    hh.delete(100)
    
    while not hh.empty():
        print hh.poll()
   



        

