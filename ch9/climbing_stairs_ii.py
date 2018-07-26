"""
Description
A child is running up a staircase with n steps, 
and can hop either 1 step, 2 steps, or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up the stairs.

Example
n=3
1+1+1=2+1=1+2=3=3
return 4
"""

class Solution:
    """
    * @param n an integer
    * @return an integer
    """
    def climbStairs2(self, n):
        if n is None:
            return 0

        f = [1 for i in xrange(n+1)]

        for i in xrange(2, n+1):
            f[i] = f[i-1] + f[i-2]
            if i > 2:
                f[i] = f[i] + f[i-3]

        return f[n]


if __name__ == '__main__':
    sol = Solution()

    print sol.climbStairs2(2)
    print sol.climbStairs2(3)
