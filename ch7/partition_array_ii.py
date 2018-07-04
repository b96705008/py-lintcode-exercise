"""
Description
Partition an unsorted integer array into three parts:

The front part < low
The middle part >= low & <= high
The tail part > high
Return any of the possible solutions.


Notice
low <= high in all testcases.


Example
Given [4,3,4,1,2,3,1,2], and low = 2 and high = 3.

Change to [1,1,2,3,2,3,4,4].
xw
([1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not)



Challenge
Do it in place.
Do it in one pass (one loop).
"""

class Solution:
    """
     * @param nums an integer array
     * @param low an integer
     * @param high an integer
     * @return nothing
    """
    def partition(self, nums, low, high):
        if nums == None or len(nums) == 0:
            return

        start = 0
        end = len(nums) - 1
        i = 0
        while i < end:
            if nums[i] < low:
                nums[start], nums[i] = nums[i], nums[start]
                start = start + 1
                i = i + 1
            elif nums[i] > high:
                nums[end], nums[i] = nums[i], nums[end]
                end = end - 1
            else:
                i = i + 1 # skip when low <= i <= high


if __name__ == '__main__':
    sol = Solution()

    nums = [4,3,4,1,2,3,1,2]
    sol.partition(nums, 2, 3)
    print nums
    
    nums = [5, 5, 3, 2, 1, 0, 0, 2, 4, 4, 3, 3]
    sol.partition(nums, 2, 4)
    print nums



