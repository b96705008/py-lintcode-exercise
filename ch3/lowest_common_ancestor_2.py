"""
Description
Given the root and two nodes in a Binary Tree. 
Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node 
with largest depth which is the ancestor of both nodes.

The node has an extra attribute parent 
which point to the father of itself. 
The root's parent is null.


Example
For the following binary tree:

  4
 / \
3   7
     / \
   5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
"""

from binary_tree import TreeNode, inorder_print

# create tree 1
root1 = TreeNode(4)

root1.left = TreeNode(3)
root1.left.parent = root1

root1.right = TreeNode(7)
root1.right.parent = root1

root1.right.left = TreeNode(5)
root1.right.left.parent = root1.right

root1.right.right = TreeNode(6)
root1.right.right.parent = root1.right


def lowest_common_ancestor(root, A, B):
	depth = {}

	def find_depth(node):
		d = 0
		cur_node = node
		while cur_node is not None:
			d += 1
			cur_node = cur_node.parent
		return d

	a_h = find_depth(A)
	b_h = find_depth(B)

	cur_a = A
	cur_b = B
	ancestor = None
	while a_h > 0 and b_h > 0:
		if a_h > b_h:
			cur_a = cur_a.parent
			a_h = a_h - 1
		elif a_h < b_h:
			cur_b = cur_b.parent
			b_h = b_h - 1
		elif cur_a != cur_b:
			cur_a = cur_a.parent
			a_h = a_h - 1
			cur_b = cur_b.parent
			b_h = b_h - 1
		else:
			ancestor = cur_a
			break

	return ancestor

print lowest_common_ancestor(root1, root1.left, root1.right.left).val == 4
print lowest_common_ancestor(root1, root1.right.left, root1.right.right).val == 7
print lowest_common_ancestor(root1, root1.right.right, root1.right).val == 7










