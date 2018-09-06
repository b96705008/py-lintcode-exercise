class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target > nums[mid]:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end

        return -1


if __name__ == '__main__':
    sol = Solution()
    
    arr = [1, 2, 4, 6, 7, 9]
    print sol.findPosition(arr, 4), 2
    print sol.findPosition(arr, 1), 0
    print sol.findPosition(arr, 9), 5

    arr = [1, 2, 2, 3, 4]
    print sol.findPosition(arr, 2)

