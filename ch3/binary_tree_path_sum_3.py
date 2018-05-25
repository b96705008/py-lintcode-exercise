"""
Description
Give a binary tree, and a target number, 
find all path that the sum of nodes equal to target, 
the path could be start and end at any node in the tree.

Example 1
Given binary tree:

    1
   / \
  2   3
 /
4
and target = 6. Return :

[
  [2, 4],
  [2, 1, 3],
  [3, 1, 2],
  [4, 2]
]

Example 2
Given binary tree:

  3
 / \
7   4
   / \
  1   2

and target = 7. Return :

[
  [7],
  [3, 4],
  [4, 3],
  [1, 4, 2],
  [2, 4, 1]
]
"""

from binary_tree import TreeNode, inorder_print

# create tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(4)
root1.right = TreeNode(3)

# create tree 2
root2 = TreeNode(3)
root2.left = TreeNode(7)
root2.right = TreeNode(4)
root2.right.left = TreeNode(1)
root2.right.right = TreeNode(2)


def get_up_paths(root):
    curr_paths = []

    if root is None:
        return curr_paths

    curr_paths.append([root.val])

    up_paths = [
        p + [root.val]
        for p in get_up_paths(root.left) + \
            get_up_paths(root.right)
    ]

    curr_paths.extend(up_paths)
    return curr_paths

def get_down_paths(root):
    curr_paths = []

    if root is None:
        return curr_paths

    curr_paths.append([root.val])

    down_paths = [
        [root.val] + p
        for p in get_down_paths(root.left) + \
            get_down_paths(root.right)
    ]

    curr_paths.extend(down_paths)
    return curr_paths


def find_sum_paths(root, target):
    paths = []

    def traverse(root, target, paths):
        if root is None:
            return

        if root.val == target:
            paths.append([root.val])

        # clockwise
        for p in [ 
            r + [root.val] + l
            for r in [[]] + get_up_paths(root.right)
            for l in [[]] + get_down_paths(root.left)
            if len(r) != 0 or len(l) != 0]:
            if sum(p) == target:
                paths.append(p)

        # counter clockwise
        for p in [
            l + [root.val] + r
            for l in [[]] + get_up_paths(root.left)
            for r in [[]] + get_down_paths(root.right)
            if len(r) != 0 or len(l) != 0]:
            if sum(p) == target:
                paths.append(p)
                                                               
        traverse(root.left, target, paths)
        traverse(root.right, target, paths)

    traverse(root, target, paths)
    return paths


def testing(root, target):
    paths = find_sum_paths(root, target)
    is_valid = all(map(lambda p: sum(p)==target, paths))
    print target, is_valid, paths

testing(root1, 6)
testing(root1, 3)
testing(root1, 4)
testing(root2, 7)
testing(root2, 14)



