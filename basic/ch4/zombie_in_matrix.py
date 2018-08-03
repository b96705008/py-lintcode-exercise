"""
Description
Given a 2D grid, each cell is either a wall 2, 
a zombie 1 or people 0 (the number zero, one, two).
Zombies can turn the nearest people(up/down/left/right) 
into zombies every day, but can not through wall. 
How long will it take to turn all people into zombies? 
Return -1 if can not turn all people into zombies.

Example
Given a matrix:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
return 2
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


def change_zombies(grid):
    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2

    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return -1

    n_row = len(grid)
    n_col = len(grid[0])
    new_grid = copy_grid(grid)

    delta_num = 4
    delta_i = [0, 1, 0, -1]
    delta_j = [1, 0, -1, 0]

    queue = []
    people_num = 0
    days = 0

    # find all zombies and people
    for i in range(n_row):
        for j in range(n_col):
            thing = new_grid[i][j]
            if thing == PEOPLE:
                people_num = people_num + 1
            elif thing == ZOMBIE:
                queue.append(Point(i, j))

    # Zombies eat people using BFS
    while len(queue) > 0:
        days = days + 1
        zombie_num = len(queue)

        # iterate every zombie
        while zombie_num > 0:
            zombie = queue.pop(0)
            zombie_num = zombie_num - 1

            # check and eat nearest people
            for d in range(delta_num):
                new_zombie = zombie.move(delta_i[d], delta_j[d])

                if not is_within_bound(new_grid, new_zombie):
                    continue

                if new_grid[new_zombie.i][new_zombie.j] == PEOPLE:
                    # eat 1 person
                    new_grid[new_zombie.i][new_zombie.j] = ZOMBIE
                    queue.append(new_zombie)
                    people_num = people_num - 1
                    if people_num == 0:
                        return days        

    return days if people_num == 0 else -1


# example
grid = [
    [0,1,2,0,0],
    [1,0,0,2,1],
    [0,1,0,0,0]]
print change_zombies(grid), 2
        
# example
grid = [
    [0,1,2,0],
    [1,0,0,2],
    [0,1,0,1]]
print change_zombies(grid), -1


# example
grid = [
    [0,1,0,1],
    [1,0,1,2],
    [0,1,0,1]]
print change_zombies(grid), 1


