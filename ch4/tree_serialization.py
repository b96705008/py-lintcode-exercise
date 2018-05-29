class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_print(root):
    if root is not None:
        inorder_print(root.left)
        print root.val,
        inorder_print(root.right)

def serialize(root):
    # write your code here
    values = []
    if root is None:
        return ','.join(values)
    
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)

        if node is None:
            values.append('#')
            continue

        values.append(str(node.val))
        queue.append(node.left)
        queue.append(node.right)

    i = len(values) - 1
    while values[i] == '#':
        i = i - 1

    return ','.join(values[:i+1])


def deserialize(data):
    # write your code here
    root = None
    values = [] if data is None or data == '' else data.split(',')

    if len(values) == 0:
        return root
    
    # 1. init e
    root = TreeNode(int(values.pop(0)))
    queue = [(root, 'left'), (root, 'right')]
    
    # 2. while loop
    i = 0
    while i < len(values):
        status = queue.pop(0)
        value = values[i]
        i = i + 1
        if value == '#':
            continue
       
        node = TreeNode(int(value))
        setattr(status[0], status[1], node)
        queue.extend([(node, 'left'), (node, 'right')])
        
    return root


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.left.right.left = TreeNode(6)
root1.right = TreeNode(3)
root1.right.right = TreeNode(5)

ser = serialize(root1)
print ser

root2 = deserialize(ser)
inorder_print(root2); print ''
ser = serialize(root2)
print ser

ser = serialize(None)
print ser

root2 = deserialize(ser)
inorder_print(root2); print ''
ser = serialize(root2)
print ser
