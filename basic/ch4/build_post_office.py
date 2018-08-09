"""
Problem
Given a 2D grid, each cell is either an house 1 or empty 0 
(the number zero, one), 
find the place to build a post office, 
the distance that post office to all the house sum is smallest. 
Return the smallest distance. 
Return -1 if it is not possible.

Notice
You can pass through house and empty.
You only build post office on an empty.

Example
Given a grid:

0 1 0 0
1 0 1 1
0 1 0 0
return 6. (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)
"""

EMPTY = 0
HOUSE = 1

class OfficePoint(object):

    def __init__(self, i, j):
        # original (i, j)
        self.o_i = i
        self.o_j = j
        self.c_i = i
        self.c_j = j

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
        return op

    @property
    def distance(self):
        return abs(self.c_i - self.o_i) + abs(self.c_j - self.o_j)

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

    # BFS find smallest place
    place = None
    min_dist_sum = float('inf')

    while len(queue):
        point_num = len(queue)

        while point_num > 0:
            point = queue.pop(0)
            point_num = point_num - 1
            
            for d in range(delta_num):
                new_point = point.move(delta_i[d], delta_j[d])

                if not is_within_bound(grid, new_point) or \
                    new_point.current in visited[new_point.origin]: 
                    continue

                if grid[new_point.c_i][new_point.c_j] == HOUSE:
                    house_dists[new_point.origin].append(new_point.distance)
                    if len(house_dists[new_point.origin]) == house_num:
                        dist_sum = sum(house_dists[new_point.origin])
                        if dist_sum < min_dist_sum:
                            min_dist_sum = dist_sum
                            place = new_point.origin

                queue.append(new_point)
                visited[new_point.origin].add(new_point.current)

    # find smallest sum
    return (None, -1) if place is None else (place, min_dist_sum)
    

if __name__ == '__main__':
    grid = [
        [0,1,0,0],
        [1,0,1,1],
        [0,1,0,0]]
    print build_office(grid)

    grid = [
        [0,1,1],
        [0,1,1],
        [1,0,0]]
    print build_office(grid)





