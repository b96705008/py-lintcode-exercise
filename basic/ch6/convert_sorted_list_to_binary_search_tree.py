"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:

"""
from list_node import *


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def inorder_print(root):
    if root is not None:
        inorder_print(root.left)
        print root.val,
        inorder_print(root.right)

class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def find_mid(self, head, tail):
        slow = head
        fast = head.next
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
            
        return slow

    
    def build_BST(self, head, tail):
        # 0 or 1
        if head == tail:
            return None

        if head.next == tail:
            return TreeNode(head.val)

        mid = self.find_mid(head, tail)
        root = TreeNode(mid.val)
        root.left = self.build_BST(head, mid)
        root.right = self.build_BST(mid.next, tail)        
        return root

            
    def sortedListToBST(self, head):
        # write your code here
        if head is None:
            return None
        
        root = self.build_BST(head, None)
        return root


if __name__ == '__main__':
    sol = Solution()

    head = create_linked_list(range(1, 10))
    print_list(head)
    root = sol.sortedListToBST(head)
    inorder_print(root)
    print ''
    
