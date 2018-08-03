"""
Description
Given an array of integers, remove the duplicate numbers in it.

You should:
1. Do it in place in the array.
2. Move the unique numbers to the front of the array.
3. Return the total number of the unique numbers.


Notice
You don't need to keep the original order of the integers.


Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, 
we only care about the part which has no duplicate integers.


Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
"""

class Solution:
    """
    @param nums an array of integers
    @return the number of unique integers
    """
    def deduplication(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        n = len(nums)

        # method 1: O(n) with hashset
        # visited = set()
        # unique_cnt = 0
        # l = 0
        # r = l
        # while l < n and r < n:
        #     while l < n and nums[l] not in visited:
        #         visited.add(nums[l])
        #         unique_cnt = unique_cnt + 1
        #         l = l + 1

        #     r = l + 1
        #     while r < n and nums[r] in visited:
        #         r = r + 1

        #     if l < n and r < n:
        #         nums[l], nums[r] = nums[r], nums[l]

        # method 2: O(nlogn) without extra space
        nums.sort() 
        unique_cnt = 1
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l = l + 1
                nums[l], nums[r] = nums[r], nums[l]
                unique_cnt = unique_cnt + 1

        print nums, unique_cnt
        return unique_cnt


if __name__ == '__main__':
    sol = Solution()
    
    nums = [1,3,1,4,4,2]
    sol.deduplication(nums)

    nums = [5,3,1,1,4,4,2,2]
    sol.deduplication(nums)

    nums = [1,1,2,2,2,3,3,3,3,6,7,8,9]
    sol.deduplication(nums)






