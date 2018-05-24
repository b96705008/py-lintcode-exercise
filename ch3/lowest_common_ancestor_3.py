"""
Given the root and two nodes in a Binary Tree. 
Find the lowest common ancestor(LCA) of the two nodes. 
The lowest common ancestor is the node with largest depth 
which is the ancestor of both nodes.

Return null if LCA does not exist.

Notice: node A or node B may not exist in tree.

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
root1.right = TreeNode(7)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(6)


def find_lowest_common_ancestor(root, v1, v2):
	lca = None
	paths = {}

	if v1 is None or v2 is None:
		return lca

	def traverse(root, values, prefix, paths):
		if root is None:
			return

		prefix.append(root.val)
		if root.val in values:
			paths[root.val] = prefix[:] # snapshot

		traverse(root.left, values, prefix, paths)
		traverse(root.right, values, prefix, paths)
		prefix.pop() # back track

	traverse(root, [v1, v2], [], paths)

	if v1 not in paths or v2 not in paths:
		return lca

	i = 0
	j = 0
	while i < len(paths[v1]) and j < len(paths[v2]):
		if paths[v1][i] == paths[v2][j]:
			lca = paths[v1][i]
		else:
			break
		i += 1
		j += 1

	return lca


print find_lowest_common_ancestor(root1, 3, 5) == 4
print find_lowest_common_ancestor(root1, 5, 6) == 7
print find_lowest_common_ancestor(root1, 6, 7) == 7
print find_lowest_common_ancestor(root1, 3, 6) == 4

