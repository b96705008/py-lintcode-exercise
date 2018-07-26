"""
Given a knight in a chessboard n * m 
(a binary matrix with 0 as empty and 1 as barrier). 
the knight initial position is (0, 0) and he wants to reach position (n-1, m-1). 
Find the shortest path to the destination position, 
return the length of the route. Return -1 if knight can not reached.

 
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)

Example
[[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]

Return 3

[[0,0,0,0],
 [0,0,0,0],
 [0,1,0,0]]

Return -1
"""

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b


class Solution:

    dir_num = 4
    dir_x = [1,-1,2,-2]
    dir_y = [2,2,1,1]

    def is_within_grid(self, grid, point):
        n = len(grid)
        m = len(grid[0])
        return point.x >=0 and point.x < n and \
            point.y >= 0 and point.y < m

    def shortestPath2(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        #return self.run_BFS(grid)
        return self.run_DP(grid)

    def run_BFS(self, grid):
        n = len(grid)
        m = len(grid[0])
        src = Point(0, 0)
        dst = Point(n-1, m-1)
        step = 0
        queue = [src]

        # BFS
        while len(queue) > 0:
            point_num = len(queue)

            for i in xrange(0, point_num):
                point = queue.pop(0)
                if point.x == dst.x and point.y == dst.y:
                    return step

                for d in xrange(self.dir_num):
                    neighbor = Point(point.x + self.dir_x[d],
                                     point.y + self.dir_y[d])

                    if not self.is_within_grid(grid, neighbor):
                        continue

                    if grid[neighbor.x][neighbor.y] == 0:
                        queue.append(neighbor)
                        grid[neighbor.x][neighbor.y] = 1

            step = step + 1

        return -1

    def run_DP(self, grid):
        n = len(grid)
        m = len(grid[0])

        # f[x][y] = shortest step from (0,0) to (x,y)
        f = []
        for i in xrange(n):
            f.append([float('inf') for j in xrange(m)])
        f[0][0] = 0

        for j in xrange(m):
            for i in xrange(n):
                if i == 0 and j == 0:
                    continue

                if grid[i][j] == 1:
                    continue

                for d in xrange(self.dir_num):
                    point = Point(i - self.dir_x[d],
                                  j - self.dir_y[d])

                    if not self.is_within_grid(grid, point):
                        continue

                    f[i][j] = min(f[i][j], f[point.x][point.y]+1)

        return -1 if f[n-1][m-1] == float('inf') else f[n-1][m-1]


if __name__ == '__main__':
    sol = Solution()

    # example 1
    grid = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    print sol.shortestPath2(grid)

    # example 2
    grid = [
        [0,0,0,0],
        [0,0,0,0],
        [0,1,0,0]]
    print sol.shortestPath2(grid)











