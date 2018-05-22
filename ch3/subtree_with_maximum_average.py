"""
Given a binary tree, find the subtree with maximum average. 
Return the root of the subtree.

Example 
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.
"""

from binary_tree import TreeNode, preorder_print

# create tree 1
root1 = TreeNode(1)
root1.left = TreeNode(-5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)
root1.right = TreeNode(11)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(-2)

# create tree 1
root2 = TreeNode(6)
root2.left = TreeNode(-10)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(2)
root2.right = TreeNode(50)
root2.right.left = TreeNode(20)
root2.right.right = TreeNode(-2)

def find_max_avg(root):

    def traverse(root):

        if root is None:
            return {
                'sub_sum': 0.,
                'count': 0.,
                'max_root': None,
                'max_avg': float('-inf')
            }

        l_r = traverse(root.left)
        r_r = traverse(root.right)
        root_r = {
            'sub_sum': root.val + l_r['sub_sum'] + r_r['sub_sum'],
            'count': 1. + l_r['count'] + r_r['count'],
            'max_root': root.val
        }
        root_r['max_avg'] = root_r['sub_sum'] / root_r['count']

        max_r = l_r if l_r['max_avg'] > r_r['max_avg'] else r_r
        if root_r['max_avg'] < max_r['max_avg']:
            root_r['max_root'] = max_r['max_root']
            root_r['max_avg'] = max_r['max_avg']

        return root_r

    result = traverse(root)
    return result['max_root']

print find_max_avg(root1) 
print find_max_avg(root2) 
