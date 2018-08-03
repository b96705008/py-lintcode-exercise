"""
Description
Given a node from a cyclic linked list which has been sorted, 
write a function to insert a value into the list such that it remains a cyclic sorted list. 
The given node can be any single node in the list. 
Return the inserted new node.


Notice
3->5->1 is a cyclic list, so 3 is next node of 1.
3->5->1 is same with 5->1->3


Example
Given a list, and insert a value 4:
3->5->1
Return 5->1->3->4
"""


from list_node import *


def print_cyc_list(head):
    first = head
    print first.val, '->',

    curr = first.next
    while curr != first:
        print curr.val, '->',
        curr = curr.next
    print curr.val


def prepare_dataset(vals):
    dummy = ListNode('D')
    curr = dummy
    for v in vals:
        node = ListNode(v)
        curr.next = node
        curr = curr.next
    curr.next = dummy.next
    return dummy.next


class Solution:
    """
    @param head: The head of cyclic linked list.
    @param label: node label need to be inserted
    @return: head of list
    """
    def insert_cyclic_linked_list(self, head, val):
        if head is None:
            node = ListNode(val)
            node.next = node
            return node

        first, last = self.find_bound(head)
        self.insert_node(first, last, val)
        return head


    def find_bound(self, head):
        first = None
        last = None
        prev_increasing = None
        prev = head
        curr = prev.next
        while curr is not None:
            if curr.val < prev.val:
                first = curr
                last = prev
                break
            prev = curr
            curr = curr.next
        
        if first is None or last is None:
            first = head
            last = head.next

        return first, last

    def insert_node(self, first, last, val):
        node = ListNode(val)
        if val <= first.val or val >= last.val:
            node.next = first
            last.next = node
            return

        prev = first
        curr = first.next
        while curr != first:
            if prev.val < val and curr.val > val:
                node.next = curr
                prev.next = node
                break
            prev = curr
            curr = curr.next


if __name__ == '__main__':
    sol = Solution()

    # prepare dataset
    head = prepare_dataset([3, 5, 1])
    head = sol.insert_cyclic_linked_list(head, 0)
    print_cyc_list(head)

    head = sol.insert_cyclic_linked_list(None, 5)
    print_cyc_list(head)


