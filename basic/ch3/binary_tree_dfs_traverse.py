from binary_tree import insert_node 

def preorder(root):
    values = []
    if root is None:
        return values
    
    stack = []
    stack.append(root)
    
    while len(stack) != 0:
        node = stack.pop()
    
        values.append(node.val)
        
        if node.right is not None:
            stack.append(node.right)
        
        if node.left is not None:
            stack.append(node.left)
      
    return values

if __name__ == '__main__':
    print '== Create tree ==='
    root = None
    for n in [4, 2, 6, 1, 3, 5, 7]:
        root = insert_node(root, n)
    nodes = preorder(root)
    print nodes     