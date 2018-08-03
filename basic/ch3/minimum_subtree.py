"""
Given a binary tree, find the subtree with minimum sum. 
Return the root of the subtree.

Example 
Given a binary tree:
         1
       /   \
     -5     2
     / \   /  \
    0   2 -4  -5 
return the node 1.
"""

from binary_tree import TreeNode, preorder_print

# create tree 1
root1 = TreeNode(1)
root1.left = TreeNode(-5)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(2)
root1.right = TreeNode(2)
root1.right.left = TreeNode(-4)
root1.right.right = TreeNode(-5)

# create tree 1
root2 = TreeNode(6)
root2.left = TreeNode(-10)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(2)
root2.right = TreeNode(50)
root2.right.left = TreeNode(20)
root2.right.right = TreeNode(-2)


def find_minimum_subtree(root):

    def find(root):
        result = {
            'sub_sum': 0,
            'min_sum': float('inf'),
            'min_root': None
        }

        if root is None:
            return result

        left_result = find(root.left)
        right_result = find(root.right)

        root_sum = root.val + left_result['sub_sum'] + right_result['sub_sum']
        root_result = {
            'sub_sum': root_sum,
            'min_sum': root_sum,
            'min_root': root.val
        }

        smaller_result = left_result 
        if right_result['min_sum'] < left_result['min_sum']:
            smaller_result = right_result

        if smaller_result['min_root'] is not None and \
            root_result['min_sum'] > smaller_result['min_sum']:
            root_result['min_sum'] = smaller_result['min_sum']
            root_result['min_root'] = smaller_result['min_root']

        return root_result

    result = find(root)
    print result
    return result['min_root']


root_val = find_minimum_subtree(root1)
print root_val, root_val==1

root_val = find_minimum_subtree(root2)
print root_val, root_val==-10






    







