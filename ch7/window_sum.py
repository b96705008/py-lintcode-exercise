"""
Description
Given an array of n integer, and a moving window(size k), 
move the window at each iteration from the start of the array, 
find the sum of the element inside the window at each moving.

Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
"""


class Solution:
    """
     * @param nums a list of integers.
     * @return the sum of the element inside the window at each moving.
    """
    def window_sum(self, nums, k):
        if nums is None or len(nums) < k:
            return []

        windows = []
        curr_sum = 0

        # method 1: general
        # for i, n in enumerate(nums):
        #     curr_sum = curr_sum + n
        #     if i >= k:
        #         curr_sum = curr_sum - nums[i-k]

        #     if i >= k-1:
        #         windows.append(curr_sum)

        # method 2: two pointers
        i = 0
        while i < k:
            curr_sum = curr_sum + nums[i]
            i = i + 1
        windows.append(curr_sum)

        tail = k
        head = 0
        while tail < len(nums):
            curr_sum = curr_sum + nums[tail] - nums[head]
            windows.append(curr_sum)
            tail = tail + 1
            head = head + 1

        return windows


if __name__ == '__main__':
    sol = Solution()

    print sol.window_sum([1,2,7,8,5], 3), [10,17,20]
    print sol.window_sum([1,2,7,8,5], 4), [18, 22]
    print sol.window_sum([1,2], 3), []