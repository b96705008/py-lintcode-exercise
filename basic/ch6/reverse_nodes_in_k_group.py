"""
Description
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
 
Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
from list_node import *


class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if k is None or k <= 1:
            return head

        dummy = ListNode('dummy', head)

        left = dummy
        while left != None:
            left = self.reverse_and_return_left(k, left)

        return dummy.next

    def reverse_and_return_left(self, k, left):
        # compute k group bound
        last = self.compute_group_last(k, left)
        if last is None:
            return None 

        # bound 
        right = last.next
        first = left.next

        # reverse group
        curr_node = first.next
        prev_node = first
        for i in range(k-1):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # concat bound
        first.next = right
        left.next = last
        return first

    def compute_group_last(self, k, left):
        last = left
        i = 0
        while i < k and last is not None:
            last = last.next
            i = i + 1

        return last


if __name__ == '__main__':
    sol = Solution()
    head = create_linked_list(range(1, 6))
    new_head = sol.reverseKGroup(head, 2)
    print_list(new_head)

    head = create_linked_list(range(1, 6))
    new_head = sol.reverseKGroup(head, 3)
    print_list(new_head)

    head = create_linked_list(range(1, 10))
    new_head = sol.reverseKGroup(head, 3)
    print_list(new_head)

    head = create_linked_list(range(1, 6))
    new_head = sol.reverseKGroup(head, 4)
    print_list(new_head)
