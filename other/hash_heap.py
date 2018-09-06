class Node:

    def __init__(self, index, cnt):
        self.index = index
        self.cnt = cnt


class HashHeap:

    def __init__(self, desc=False):
        self.desc = desc
        self.heap = []
        self.hash = {}
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
        return len(self.heap)

    def top(self):
        return self.heap[0]

    def contains(self, val):
        return val in self.hash

    def push(self, val):
        self.size += 1

        if val in self.hash:
            self.hash[val].cnt += 1
        else:
            self.heap.append(val)
            self.hash[val] = Node(self.qsize()-1, 1)
            self._shift_up(self.qsize()-1)

    def pop(self):
        self.size -= 1
        val = self.top()
        node = self.hash[val]

        if node.cnt == 1:
            self._swap(0, self.qsize()-1)
            self.heap.pop()
            del self.hash[val]
            if not self.empty():
                self._shift_down(0)
        else:
            node.cnt -= 1

        return val

    def delete(self, val):
        self.size -= 1
        node = self.hash[val]

        if node.cnt == 1:
            index = node.index
            self._swap(index, self.qsize()-1)
            self.heap.pop()
            del self.hash[val]

            # in the middlde
            if index < self.qsize():
                self._shift_up(index)
                self._shift_down(index)
        else:
            node.cnt -= 1

    def _smaller(self, i1, i2):
        if not self.desc:
            return self.heap[i1] < self.heap[i2]
        else:
            return self.heap[i2] < self.heap[i1]

    def _swap(self, i1, i2):
        v1 = self.heap[i1]
        v2 = self.heap[i2]
        n1 = self.hash[v1]
        n2 = self.hash[v2]
        # swqp hash
        n1.index = i2
        n2.index = i1
        # swap heap
        self.heap[i1] = v2
        self.heap[i2] = v1

    def _shift_up(self, index):
        while index > 0:
            parent = self.parent_index(index)
            if not self._smaller(index, parent):
                break
            self._swap(index, parent)
            index = parent

    def _shift_down(self, index):
        while self.left_index(index) < self.qsize():
            index
            left = self.left_index(index)
            right = self.right_index(index)

            child = left
            if right < self.qsize() and self._smaller(right, child):
                child = right

            if self._smaller(child, index):
               self._swap(child, index)
               index = child
            else:
                break


if __name__ == '__main__':
    print '=== Min HashHeap =='
    # hh = HashHeap()
    # hh.push(1)
    # hh.push(80)
    # hh.push(60)
    # hh.push(90)
    # hh.push(70)
    # hh.push(75)
    # hh.push(100)
    # hh.push(150)
    # hh.delete(60)
    # print hh.pop()
    # print hh.pop()

    # hh.delete(100)

    # while not hh.empty():
    #     print hh.pop()

    print '=== Max HashHeap =='
    hh = HashHeap(True)
    hh.push((1, 0))
    hh.push((2, 0))
    hh.push((2, 1))
    print hh.pop()

    hh.push((7, 3))
    hh.delete((1, 0))
    while not hh.empty():
        print hh.pop()

   



        

