
from binary_tree import TreeNode, inorder_print

# create tree 1
root1 = TreeNode(98)
root1.left = TreeNode(97)
root1.left.left = TreeNode(88)

# create tree 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right = TreeNode(5)
root2.right.right = TreeNode(6)


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if root is None:
            return None

        # prepare left, right
        left = root.left
        right = root.right
        root.left = None
        
        self.flatten(left)
        root.right = left

        # find concat node
        mid = root
        cur_node = root.right
        while cur_node is not None:
            mid = cur_node
            cur_node = cur_node.right
        
        self.flatten(right)
        mid.right = right

    def print_flatten_tree(self, root):
        cur_node = root
        while cur_node is not None:
            print cur_node.val,
            cur_node = cur_node.right
        print ''


sol = Solution()

sol.flatten(root1)
sol.print_flatten_tree(root1)

# sol.flatten(root2)
# sol.print_flatten_tree(root2)




