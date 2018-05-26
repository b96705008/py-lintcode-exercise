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

class Status(object):

	def __init__(self, A, B):
		self.A = A
		self.B = B
		self.exist_A = False
		self.exist_B = False
		self.ancestor = None

	def set_ancestor(self, node):
		if self.ancestor is None and node is not None:
			self.ancestor = node

	def find(self, node):
		if node == self.A:
			self.exist_A = True

		if node == self.B:
			self.exist_B = True

		return self

	def exist_num(self):
		cnt = 0
		if self.exist_A:
			cnt = cnt + 1

		if self.exist_B:
			cnt = cnt + 1

		return cnt

	def merge(self, other):
		if not self.exist_A and other.exist_A:
			self.exist_A = True
		
		if not self.exist_B and other.exist_B:
			self.exist_B = True

		return self


def find_lowest_common_ancestor(root, A, B):

	if A is None or B is None:
		return None

	def divide_conquer(root, A, B):
		my_status = Status(A, B)

		if root is None:
			return my_status

		my_status.find(root)
		left = divide_conquer(root.left, A, B)
		right = divide_conquer(root.right, A, B)

		if left.exist_num() == 2:
			return left

		if right.exist_num() == 2:
			return right

		my_status.merge(left).merge(right)
		if my_status.exist_num() == 2:
			my_status.set_ancestor(root)

		return my_status

	return divide_conquer(root, A, B).ancestor


def testing(root, A, B, ans):
	result = find_lowest_common_ancestor(root1, A, B)
	if result is None:
		if ans is None:
			print True
		else:
			print False
	else:
		print result.val == ans

testing(root1, root1.left, root1.right.left, 4)
testing(root1, root1.right.left, root1.right.right, 7)
testing(root1, root1.right.right, root1.right, 7)
testing(root1, root1.left, root1.right.right, 4)
testing(root1, root1.left, TreeNode(9), None)
testing(root1, TreeNode(11), TreeNode(9), None)
testing(root1, None, root1.left, None)
