"""
Description
Given an array nums of n integers, 
find two integers in nums such that the sum is 
closest to a given number, target.

Return the difference between the sum of the two integers and the target.


Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).


Challenge
Do it in O(nlogn) time complexity.
"""

class Solution:
    """
     * @param nums an array of integer
     * @param target an integer
     * @return the difference between the sum and the target
    """
    def two_sum(self, nums, target):
        if nums is None or len(nums) < 2:
            return None

        min_diff = float('inf')
        nums.sort()
        i1 = 0
        i2 = len(nums)-1
        while i1 < i2:
            cur_sum = nums[i1] + nums[i2]
            min_diff = min(min_diff, abs(cur_sum-target))

            if cur_sum == target:
                break
            elif cur_sum < target:
                i1 = i1 + 1
            else:
                i2 = i2 - 1

        return min_diff

if __name__ == '__main__':
    sol = Solution()
    print sol.two_sum([-1, 2, 1, -4], 4), 1
    print sol.two_sum([-1, 2, 1, -4], 0), 0
    print sol.two_sum([1, -1, 2, 2], -1), 1

