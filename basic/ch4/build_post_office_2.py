"""
[Problem]

Given a 2D grid, each cell is either a wall 2, 
an house 1 or empty 0 (the number zero, one, two), 
find a place to build a post office so that the sum of the distance 
from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

Notice
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1).
 (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)
"""

EMPTY = 0
HOUSE = 1
WALL = 2


class OfficePoint(object):

    def __init__(self, i, j):
        # original (i, j)
        self.o_i = i
        self.o_j = j
        self.c_i = i
        self.c_j = j
        self.walk_len = 0

    @property
    def origin(self):
        return (self.o_i, self.o_j)

    @property
    def current(self):
        return (self.c_i, self.c_j)
    
    def move(self, delta_i, delta_j):
        op = OfficePoint(self.o_i, self.o_j)
        op.c_i = self.c_i + delta_i
        op.c_j = self.c_j + delta_j
        op.walk_len = self.walk_len + abs(delta_i) + abs(delta_j)
        return op
        

def is_within_bound(grid, point):
    n_row = len(grid)
    n_col = len(grid[0])
    if point.c_i >= 0 and point.c_i < n_row and \
        point.c_j >= 0 and point.c_j < n_col:
        return True
    else:
        return False


def build_office(grid):
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return None, -1

    # delta
    delta_num = 4
    delta_i = [0, 1, 0, -1]
    delta_j = [1, 0, -1, 0]

    # init data
    queue = []
    visited = {} # for every empty empty origin
    house_dists = {}
    n_row = len(grid)
    n_col = len(grid[0])
    house_num = 0

    # iterate all places
    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] == HOUSE:
                house_num = house_num + 1
            elif grid[i][j] == EMPTY:
                op = OfficePoint(i, j)
                queue.append(op)
                visited[op.origin] = set([op.current])
                house_dists[op.origin] = []

    place = None
    min_dist_sum = float('inf')
    while len(queue) > 0:
        point_num = len(queue)

        while point_num > 0:
            point = queue.pop(0)
            point_num = point_num - 1

            for d in range(delta_num):
                new_point = point.move(delta_i[d], delta_j[d])

                if not is_within_bound(grid, new_point) or \
                    new_point.current in visited[new_point.origin] or \
                    grid[new_point.c_i][new_point.c_j] == WALL:
                    continue

                place_type = grid[new_point.c_i][new_point.c_j]
                if place_type == HOUSE:
                    house_dists[new_point.origin].append(new_point.walk_len)
                    if len(house_dists[new_point.origin]) == house_num:
                        print new_point.origin, house_dists[new_point.origin]
                        dist_sum = sum(house_dists[new_point.origin])
                        if dist_sum < min_dist_sum:
                            min_dist_sum = dist_sum
                            place = new_point.origin
                elif place_type == EMPTY:
                    queue.append(new_point)

                visited[new_point.origin].add(new_point.current)

    return (None, -1) if place is None else (place, min_dist_sum)


if __name__ == '__main__':
    # return 8, You can build at (1,1).
    grid = [
        [0, 1, 0, 0, 0],
        [1, 0, 0, 2, 1],
        [0, 1, 0, 0, 0]]
    print build_office(grid)



