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


def find_sum_paths(root, target):
    paths = []

    def traverse(root, target, paths):
        if root is None:
            return [], []

        # recursive first
        lu_paths, ld_paths = traverse(root.left, target, paths)
        ru_paths, rd_paths = traverse(root.right, target, paths)

        # check node
        if root.val == target:
            paths.append([root.val])
 
        # clockwise check
        for p in [ 
            r + [root.val] + l
            for r in [[]] + ru_paths
            for l in [[]] + ld_paths
            if len(r) != 0 or len(l) != 0]:
            if sum(p) == target:
                paths.append(p)

        # counter clockwise check
        for p in [
            l + [root.val] + r
            for l in [[]] + lu_paths
            for r in [[]] + rd_paths
            if len(r) != 0 or len(l) != 0]:
            if sum(p) == target:
                paths.append(p)
        
        # all up paths
        up_paths = [
            up + [root.val]
            for up in [[]] + lu_paths + ru_paths
        ]

        # all down paths
        down_paths = [
            [root.val] + dp
            for dp in [[]] + ld_paths + rd_paths
        ]
        
        return up_paths, down_paths

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



