from binary_tree import TreeNode, inorder_print

# create tree 1
root1 = TreeNode(2)
root1.right = TreeNode(7)
root1.right.left = TreeNode(5)
root1.right.left = TreeNode(3)

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def find_min(self, root):
        curr_node = root
        parent = None
        while curr_node is not None:
            parent = curr_node
            curr_node = curr_node.left
        
        return parent
            
    
    def inorderSuccessor(self, root, p):
        # write your code here
        # find minist val but > p.val
        successor = None
        founded = False
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
        
            if node is None:
                continue
            
            if founded:
                successor = node
                break
            
            if p.val < node.val:
                stack.append(node)
                stack.append(node.left)
            elif p.val > node.val:
                stack.append(node.right)
            else:
                # p.val == node.val
                founded = True
                successor = self.find_min(node.right)
                stack.append(successor)
              
        return successor

sol = Solution()
suc = sol.inorderSuccessor(root1, root1)
if suc is not None:
    print suc.val
else:
    print 'not found'
