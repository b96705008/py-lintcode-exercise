"""
Description
Your are given a binary tree in which each node contains a value. 
Design an algorithm to get all paths which sum to a given value. 
he path does not need to start or end at the root or a leaf, 
but it must go in a straight line down.

Example
Given a binary tree:

    1
   / \
  2   3
 /   /
4   2
for target = 6, return

[
  [2, 4],
  [1, 3, 2]
]
"""

from binary_tree import TreeNode, inorder_print

# create tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(4)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)

def find_sum_paths(root, target):
	paths = []

	def traverse(root, target, paths, prev_seqs):
		if root is None:
			return

		curr_seqs = [s + [root.val] for s in prev_seqs + [[]]]
		for s in curr_seqs:
			if sum(s) == target:
				paths.append(s[:])


		if root.left is not None:
			traverse(root.left, target, paths, curr_seqs)

		if root.right is not None:
			traverse(root.right, target, paths, curr_seqs)

	traverse(root, target, paths, [])
	return paths


print 6, find_sum_paths(root1, 6)
print 3, find_sum_paths(root1, 3)
print 4, find_sum_paths(root1, 4)





