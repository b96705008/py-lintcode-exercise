"""
[Problem]

Given a knight in a chessboard 
(a binary matrix with 0 as empty and 1 as barrier) 
with a source position, 
find the shortest path to a destination position, 
return the length of the route. 
Return -1 if knight can not reached.

 Notice
source and destination must be empty.
Knight can not enter the barrier.

 
Clarification
If the knight is at (x, y), 
he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)

Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
"""

class Point(object):
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.i == other.i and self.j == other.j
        return False

    def move(self, i_diff, j_diff):
        return Point(self.i + i_diff, self.j + j_diff)


def is_within_bound(grid, point):
    n_row = len(grid)
    n_col = len(grid[0])
    if point.i >= 0 and point.i < n_row and \
        point.j >= 0 and point.j < n_col:
        return True
    else:
        return False


def copy_grid(grid):
    new_grid = []
    for row in grid:
        new_grid.append([e for e in row])
    return new_grid


def find_shortest_path(grid, src, dst):
    if grid is None or len(grid) == 0 or len(grid[0]) == 0 or \
        src is None or dst is None:
        return -1

    dir_num = 8
    dir_i = [1, 1, -1, -1, 2, 2, -2, -2]
    dir_j = [2, -2, 2, -2, 1, -1, 1, -1]
    step = 0
    new_grid = copy_grid(grid)

    queue = [src]
    new_grid[src.i][src.j] = 1
    # 1. init points
    while len(queue) > 0:
        point_num = len(queue)

        # 2. Iterate points in the same level
        while point_num > 0:
            point = queue.pop(0)
            if point == dst:
                return step

            # 3. go to 8 directions (next step)
            for n in range(dir_num):
                new_point = point.move(dir_i[n], dir_j[n])

                if not is_within_bound(new_grid, new_point):
                    continue

                if new_grid[new_point.i][new_point.j] == 0:
                    queue.append(new_point)
                    new_grid[new_point.i][new_point.j] = 1

            point_num = point_num - 1 
        step = step + 1
    return -1


# example 1:
grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]
print find_shortest_path(grid, Point(2,0), Point(2,2)), 2


grid = [
    [0,1,0],
    [0,0,0],
    [0,0,0]]
print find_shortest_path(grid, Point(2,0), Point(2,2)), 6


grid = [
    [0,1,0],
    [0,0,1],
    [0,0,0]]
print find_shortest_path(grid, Point(2,0), Point(2,2)), -1

