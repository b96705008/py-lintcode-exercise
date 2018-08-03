class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    head = None
    cur_node = None
    for i, v in enumerate(values):
        node = ListNode(v)
        if i == 0:
            head = node
            cur_node = node
        else:
            cur_node.next = node
            cur_node = cur_node.next

    return head


def find_mid(head, tail=None):
        slow = head
        fast = head.next
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        
        return slow

def print_list(node):
    while node is not None:
        print node.val, '->',
        node = node.next
    print 'null'


if __name__ == '__main__':
    head = create_linked_list(range(1, 4))
    print_list(head)

    # find mid
    mid = find_mid(head)
    print mid.val

    mid = find_mid(ListNode(5))
    print mid.val


    head = create_linked_list(range(0, 4))
    print_list(head)

    mid = find_mid(head, head.next.next.next)
    print mid.val

    # left_node = head
    # next_node = head.next.next
    # prev_node = head.next

    # # reverse
    # last = next_node.next
    # next_node.next = prev_node
    # prev_node.next = last
    # left_node.next = next_node

    # print_list(left_node)

    


