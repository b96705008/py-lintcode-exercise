"""
Difficulty: Easy

http://www.lintcode.com/en/problem/convert-binary-tree-to-linked-lists-by-depth/

Given a binary tree, 
design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth D, you'll have D linked lists).

Example
Given binary tree:

    1
   / \
  2   3
 /
4
return

[
  1->null,
  2->3->null,
  4->null
]
```
"""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def convert_to_lists(root):
    lists = []
    if root is None:
        return lists

    queue = [root]
    while len(queue) > 0:
        level_num = len(queue)
        head = None
        cur_node = None

        while level_num > 0:
            t_node = queue.pop(0)
            # create and append node to linked list
            if head is None:
                head = ListNode(t_node.val)
                cur_node = head
            else:
                cur_node.next = ListNode(t_node.val)
                cur_node = cur_node.next

            # add tree node children to queue
            if t_node.left is not None:
                queue.append(t_node.left)

            if t_node.right is not None:
                queue.append(t_node.right)

            level_num = level_num - 1

        lists.append(head)

    return lists


def print_list_of_linkedlist(lists):
    for n in lists:
        while n is not None:
            print '{} ->'.format(n.val),
            n = n.next
        print 'null'

print '== example 1 =='
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(4)
root1.right = TreeNode(3)
lists = convert_to_lists(root1)
print_list_of_linkedlist(lists)

print '== example 2 =='
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.right.right = TreeNode(5)
root1.left.left.right = TreeNode(6)
lists = convert_to_lists(root1)
print_list_of_linkedlist(lists)

















