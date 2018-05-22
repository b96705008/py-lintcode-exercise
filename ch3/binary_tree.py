class TreeNode(object):

	def __init__(self, val=0):
		self.val = val
		self.left = None
		self.right = None

	@property
	def child_num(self):
		num = int(self.left is not None) + \
			int(self.right is not None)
		return num


def insert_node(root, val):
	new_node = TreeNode(val)

	if root is None:
		return new_node

	curr_node = root
	parent = None
	while curr_node is not None:
		if curr_node.val == val:
			print '{} is already existed.'.format(val)
			return root

		parent = curr_node
		if curr_node.val > val:
			curr_node = curr_node.left
		else:
			curr_node = curr_node.right

	if parent.val > val:
		parent.left = new_node
	else:
		parent.right = new_node

	return root


def search(root, val):
	curr_node = root
	parent = None
	direction = None
	while curr_node is not None:
		if curr_node.val == val:
			break
		
		parent = curr_node
		if curr_node.val > val:
			curr_node = curr_node.left
			direction = 'left'
		else:
			curr_node = curr_node.right
			direction = 'right'

	return curr_node, parent, direction

def find_max(root):
	curr_node = root
	parent = None

	while curr_node is not None and \
		curr_node.right is not None:
		parent = curr_node
		curr_node = curr_node.right

	return curr_node, parent


def remove_node(root, val):
	if root is None:
		return root

	node, parent, direction = search(root, val)
	
	if node is None:
		return root

	# case 1: leaf
	if node.child_num == 0:
		if parent is None:
			root = None
		if direction == 'left':
			parent.left = None
		elif direction == 'right':
			parent.right = None
	# case 2: 1 child
	elif node.child_num == 1:
		child = node.left if node.right is None else node.right
		if parent is None:
			root = child
		elif direction == 'left':
			parent.left = child
		elif direction == 'right':
			parent.right = child
	# case 3: 2 children
	else:
		left_max, left_max_parent = find_max(node.left)
		remove_node(node, left_max.val)
		left_max.left = node.left
		left_max.right = node.right
		if parent is None:
			root = left_max
		elif direction == 'left':
			parent.left = left_max
		elif direction == 'right':
			parent.right = left_max

	return root


def inorder_print(root):
	if root is not None:
		inorder_print(root.left)
		print root.val,
		inorder_print(root.right)


def preorder_print(root):
	if root is not None:
		print root.val,
		preorder_print(root.left)
		preorder_print(root.right)


def postorder_print(root):
	if root is not None:
		postorder_print(root.left)
		postorder_print(root.right)
		print root.val,


if __name__ == '__main__':
	print '== Insert Test ==='

	root = None
	for n in [4, 2, 6, 1, 5]:
		root = insert_node(root, n)
	inorder_print(root)
	print ''

	root = insert_node(root, 3)
	root = insert_node(root, 7)
	root = insert_node(root, 6)
	inorder_print(root)
	print ''


	print '== Traverse Test ==='
	inorder_print(root)
	print ''
	preorder_print(root)
	print ''
	postorder_print(root)
	print ''

	print '== Search Test ==='
	node, _, _ = search(root, 4)
	print 4, node is not None
	node, _, _ = search(root, 1)
	print 1, node is not None

	print '== Find Max =='
	node, parent = find_max(root)
	print node.val, parent.val

	try:
		node, parent = find_max(None)
		print node.val, parent.val
	except:
		print 'node is empty'

	print '== Remove Test =='
	remove_node(root, 10)
	inorder_print(root)
	print ''

	remove_node(root, 5)
	inorder_print(root)
	print ''

	remove_node(root, 6)
	inorder_print(root)
	print ''

	root = remove_node(root, 4)
	inorder_print(root)
	print ''

	root = remove_node(root, 3)
	inorder_print(root)
	print ''

	root = remove_node(root, 2)
	inorder_print(root)
	print ''

	root = remove_node(root, 1)
	inorder_print(root)
	print ''

	root = remove_node(root, 7)
	inorder_print(root)
	print ''

