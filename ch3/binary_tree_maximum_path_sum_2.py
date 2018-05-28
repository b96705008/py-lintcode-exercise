"""
[LintCode] 475 Binary Tree Maximum Path Sum 2
Description
Given a binary tree, find the maximum path sum from root.

The path may end at any node in the tree and contain at least one node in it.

Example
Given the below binary tree:

  1
 / \
2   3
return 4. (1->3)
"""

from binary_tree import TreeNode

# create tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

# create tree 2
root2 = TreeNode(1)
root2.left = TreeNode(20)
root2.left.left = TreeNode(-10)
root2.left.right = TreeNode(-5)
root2.right = TreeNode(-9)
root2.right.left = TreeNode(20)
root2.right.right = TreeNode(-5)


def find_max_path_sum(root):

	if root is None:
		return 0

	l_max = find_max_path_sum(root.left)
	r_max = find_max_path_sum(root.right)
	return root.val + max(l_max, r_max, 0)


def testing(root, ans):
	sol = find_max_path_sum(root)
	print sol, sol==ans

testing(root1, 4)
testing(root2, 21)

