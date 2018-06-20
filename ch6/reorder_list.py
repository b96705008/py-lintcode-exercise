from list_node import *


class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
       
        # 1. split 2
        left, right = self.split_list(head)
        if right is None:
            return head
        
        # 2. reverse 2nd list
        right = self.reverse(right)
        
        # 3. concat 2 lists
        prev = self.concat(left, right)

        return prev
        
    
    def split_list(self, head):
        # compute mid
        i = 0
        curr = head 
        while curr is not None:
            i = i + 1
            curr = curr.next
        
        if i < 2:
            return head, None
    
        mid = i / 2
        if i % 2 == 1:
            mid = mid + 1
        
        # find right
        last = head
        for i in range(mid-1):
            last = last.next
        
        right = last.next
        last.next = None
        
        return head, right
    
    def reverse(self, first):
        prev = first
        curr = first.next
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        first.next = None
        return prev
    
    def concat(self, left, right):
        dummy = ListNode('dummy')
        prev = dummy
        
        i = 0
        while left is not None and right is not None:
            if i % 2 == 0:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next
            prev.next = None
            i = i + 1
        
        if left is not None:
            prev.next = left
        elif right is not None:
            prev.next = right
        
        return dummy.next
        

if __name__ == '__main__':
    sol = Solution()

    node1 = ListNode(2)
    node2 = ListNode(-1)
    node3 = ListNode(0)
    node1.next = node2
    node2.next = node3
    head = sol.reorderList(node1)
    print_list(head)

    node1 = create_linked_list(range(1, 5))
    head = sol.reorderList(node1)
    print_list(head)

        
        

