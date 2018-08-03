from list_node import *


class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        new_head = self.merge_sort(head)
        return new_head
    
    
    def merge(self, cur1, cur2):
        dummy = ListNode('D')
        cur = dummy

        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
            cur.next = None
        
        if cur1 is not None:
            cur.next = cur1
        
        if cur2 is not None:
            cur.next = cur2
        
        return dummy.next
    
    
    def split_half(self, head):
        i = 0
        curr = head
        while curr is not None:
            i = i + 1
            curr = curr.next
        
        if i < 2:
            return head, None
        
        mid = i / 2
        tail = head
        for i in range(mid-1):
            tail = tail.next
        
        right = tail.next
        tail.next = None
        
        return head, right
        
    
    def merge_sort(self, head):
        left, right = self.split_half(head)
        if right is None:
            return head
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        sub_head = self.merge(left, right)
        return sub_head
            
        
if __name__ == '__main__':
    sol = Solution()
    head = create_linked_list([4,3,2])
    new_head = sol.sortList(head)
    print_list(new_head)


    
    
    
