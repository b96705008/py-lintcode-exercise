"""
Description
Given an array of integers, 
find how many pairs in the array such that their sum is less than or equal to a specific target number. 
Please return the number of pairs.


Example
Given nums = [2, 7, 11, 15], target = 24.
Return 5.
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
"""

class Solution:
    """
     * @param nums an array of integer
     * @param target an integer
     * @return an integer
    """
    def two_sum(self, nums, target):
        count = 0
        if nums is None or len(nums) == 0:
            return count

        nums.sort()
        i1 = 0
        i2 = len(nums) - 1
        while i1 < i2:
            cur_sum = nums[i1] + nums[i2]
            if cur_sum <= target:
                count = count + (i2 - i1)
                i1 = i1 + 1
            else:
                i2 = i2 - 1

        return count

if __name__ == '__main__':
    sol = Solution()
    print sol.two_sum([2, 7, 11, 15], 24), 5
    print sol.two_sum([2, 7, 11, 15], 20), 4
    print sol.two_sum([1,1,1,1], 2), 6
